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
