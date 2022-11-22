from datetime import timedelta
from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
    AbstractUser
)
from django.db.models import Q
from django.template.loader import get_template
from django.urls import reverse
from django.utils import timezone
from django.db.models.signals import pre_save, post_save
from django.conf import settings
from .utils import unique_key_generator

DEFAULT_ACTIVATION_DAYS = getattr(settings, 'DEFAULT_ACTIVATION_DAYS', 7)


class UserManager(BaseUserManager):
    def create_user(
            self, email,
            password=None,
            first_name=None,
            last_name=None,
            dob=None,
            gender=None,
            contact_number=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            dob=dob,
            gender=gender,
            contact_number=contact_number
        )
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password, first_name, last_name, dob, gender, contact_number):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            dob=dob,
            gender=gender,
            contact_number=contact_number
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(
            self,
            email,
            password,
            first_name,
            last_name,
            dob,
            gender,
            contact_number
    ):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            dob=dob,
            gender=gender,
            contact_number=contact_number
        )
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


GENDER = [
    ('M', 'MALE'),
    ('F', 'FEMALE'),
    ('O', 'OTHER')
]


class User(AbstractUser):
    # first_name = models.CharField(max_length=100, verbose_name='First Name')
    # last_name = models.CharField(max_length=100, verbose_name='Last Name')
    username = None
    email = models.EmailField(
        verbose_name='Email Address',
        max_length=255,
        unique=True,
    )
    dob = models.DateField(auto_now_add=False,  verbose_name='Date of Birth')
    contact_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=1, choices=GENDER)
    # last_login = models.DateTimeField(default=timezone.now, verbose_name='Last Login')
    # date_joined = models.DateTimeField(default=timezone.now, verbose_name='Date Joined')
    # active = models.BooleanField(default=True)
    # staff = models.BooleanField(default=False)  # a admin user; non super-user
    # admin = models.BooleanField(default=False)  # a superuser
    # notice the absence of a "Password field", that's built in.

    USERNAME_FIELD = 'email'
    # Email & Password are required by default.
    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
        'dob', 'gender',
        'contact_number'
    ]

    objects = UserManager()

    def __str__(self):  # __unicode__ on Python 2
        return self.email


class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


class EmailActivationQuerySet(models.query.QuerySet):
    def confirmable(self):
        now = timezone.now()
        start_range = now - timedelta(days=DEFAULT_ACTIVATION_DAYS)
        # does my object have a timestamp in here
        end_range = now
        return self.filter(
            activated=False,
            forced_expired=False
        ).filter(
            timestamp__gt=start_range,
            timestamp__lte=end_range
        )


class EmailActivationManager(models.Manager):
    def get_queryset(self):
        return EmailActivationQuerySet(self.model, using=self._db)

    def confirmable(self):
        return self.get_queryset().confirmable()

    def email_exists(self, email):
        return self.get_queryset().filter(
            Q(email=email) |
            Q(user__email=email)
        ).filter(
            activated=False
        )


class EmailActivation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    key = models.CharField(max_length=120, blank=True, null=True)
    activated = models.BooleanField(default=False)
    forced_expired = models.BooleanField(default=False)
    expires = models.IntegerField(default=7)  # 7 Days
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    objects = EmailActivationManager()

    def __str__(self):
        return self.email

    def can_activate(self):
        qs = EmailActivation.objects.filter(pk=self.pk).confirmable()  # 1 object
        if qs.exists():
            return True
        return False

    def activate(self):
        if self.can_activate():
            # pre activation user signal
            user = self.user
            user.is_active = True
            user.save()
            # post activation signal for user
            self.activated = True
            self.save()
            return True
        return False

    def regenerate(self):
        self.key = None
        self.save()
        if self.key is not None:
            return True
        return False

    def send_activation(self):
        if not self.activated and not self.forced_expired:
            if self.key:
                base_url = getattr(settings, 'BASE_URL', 'https://www.belasea.com')
                key_path = reverse("account:email-activate", kwargs={'key': self.key})  # use reverse
                path = "{base}{path}".format(base=base_url, path=key_path)
                context = {
                    'path': path,
                    'email': self.email,
                    'name': self.user.first_name + ' ' + self.user.last_name
                }
                txt_ = get_template("registration/emails/verify.txt").render(context)
                html_ = get_template("registration/emails/verify.html").render(context)
                subject = '1-Click Email Verification'
                from_email = settings.DEFAULT_FROM_EMAIL
                recipient_list = [self.email]
                sent_mail = send_mail(
                    subject,
                    txt_,
                    from_email,
                    recipient_list,
                    html_message=html_,
                    fail_silently=False,
                )
                return sent_mail
        return False


def pre_save_email_activation(sender, instance, *args, **kwargs):
    if not instance.activated and not instance.forced_expired:
        if not instance.key:
            instance.key = unique_key_generator(instance)


pre_save.connect(pre_save_email_activation, sender=EmailActivation)


def post_save_user_create_receiver(sender, instance, created, *args, **kwargs):
    if created:
        obj = EmailActivation.objects.create(user=instance, email=instance.email)
        obj.send_activation()


post_save.connect(post_save_user_create_receiver, sender=User)
