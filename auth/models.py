from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=255)
    orgs = models.ManyToManyField(
        'auth.Organization',
        related_name='users',
    )
    
    
class Organization(models.Model):
    name = models.CharField(max_length=255)
