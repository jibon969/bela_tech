from django.db import models


class Slider(models.Model):
    title = models.CharField(max_length=120)
    image = models.FileField()
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']


class Service(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    icon = models.CharField(max_length=100, help_text="fa fa-home")
    value = models.PositiveIntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']


class WorkCounter(models.Model):
    title = models.CharField(max_length=100)
    work_complete = models.PositiveBigIntegerField(default=1)
    year_experience = models.PositiveBigIntegerField(default=2)
    total_client = models.PositiveBigIntegerField(default=1)
    award = models.PositiveBigIntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']


class Project(models.Model):
    title = models.CharField(max_length=120)
    image = models.FileField()
    project_url = models.URLField(blank=True, null=True)
    project_type = models.CharField(max_length=120)
    value = models.PositiveIntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']


class Testimonial(models.Model):
    name = models.CharField(max_length=120)
    image = models.FileField()
    message = models.TextField()
    value = models.PositiveIntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-timestamp']


class Team(models.Model):
    name = models.CharField(max_length=120)
    designation = models.CharField(max_length=120)
    image = models.FileField()
    facebook_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    website_url = models.URLField(blank=True, null=True)
    value = models.PositiveIntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-timestamp']


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    subject = models.CharField(max_length=240)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-timestamp']


class Replay(models.Model):
    send_to = models.EmailField(max_length=100, blank=True, null=True)
    subject = models.CharField(max_length=120)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
