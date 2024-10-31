from django.db import models

class Footer(models.Model):
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=30)
    instagram = models.CharField(max_length=50)
    telegram = models.CharField(max_length=30)

class Message(models.Model):
    fname = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return f"{self.fname} - {self.email}"