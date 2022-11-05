from django.db import models

# Create your models here.
class Members(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
# class Bosses(models.Model):
#     address = models.CharField(max_length=255)
#     telephone = models.CharField(max_length=255)
