from django.db import models

# Create your models here.
class UserInfo(models.Model):
    id=models.IntegerField(primary_key=True)
    first_name=models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    age=models.IntegerField()
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip=models.IntegerField()
    email=models.EmailField(max_length=100)
    web=models.URLField(max_length=150)


# users/models.py
#from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)


# class User(AbstractBaseUser, PermissionsMixin):
#     """
#     An abstract base class implementing a fully featured User model with
#     admin-compliant permissions.
#
#     """
#     email = models.EmailField(max_length=40, unique=True)
#     first_name = models.CharField(max_length=30, blank=True)
#     last_name = models.CharField(max_length=30, blank=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     date_joined = models.DateTimeField(default=timezone.now)
#
#     objects = UserManager()
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name']
#
#     def save(self, *args, **kwargs):
#         super(User, self).save(*args, **kwargs)
#         return self
