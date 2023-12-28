from django.db import models

# Create your models here.
class Employee(models.Model):
    org = models.ForeignKey(
        'auth.Organization', related_name='employees',
        on_delete=models.CASCADE,
    )
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = models.IntegerField()
    department = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
