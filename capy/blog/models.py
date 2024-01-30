from django.db import models

# Create your models here.
class hit1(models.Model):

    title = models.CharField(max_length=200, default="x")
    name = models.CharField(max_length=200, default="x")
    prispevek = models.CharField(max_length=200, default="x")



