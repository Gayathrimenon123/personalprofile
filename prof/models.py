from django.db import models

# Create your models here.
class prof(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    mca = models.CharField(max_length=2550)
    bca = models.CharField(max_length=255)
    twelth = models.CharField(max_length=255)
    tenth = models.CharField(max_length=255)
    lang = models.CharField(max_length=255)