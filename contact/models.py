from django.db import models
from django.contrib.auth.models import User

from django.utils.text import slugify

# Create your models here.
class Info(models.Model):
    place = models.CharField(max_length=50,blank=True,null=True)
    phone_number = models.CharField(max_length=20,blank=True,null=True)
    email = models.EmailField(max_length=254,blank=True,null=True)


    class Meta:
        verbose_name = ("Info")
        verbose_name_plural = ("Infos")

    def __str__(self):
        return self.email

