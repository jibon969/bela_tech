from django.db import models


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
