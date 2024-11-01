from django.db import models
from django.template.context_processors import request


class Project(models.Model):
    title= models.CharField(max_length=25,)
    description= models.CharField(max_length=35)
    address= models.CharField(max_length=140)
    image = models.ImageField(upload_to="projects/")

    def __str__(self):
        return self.title


class RequestedProject(models.Model):
    name = models.CharField(max_length=25,)
    email = models.EmailField()
    description = models.TextField()
    body = models.TextField()
    def __str__(self):
        return self.name