from django.db import models

STATUS_ACTIVE = 'Active'
STATUS_NOT_STARTED = 'Not Started'
STATUS_TERMINATED = 'Terminated'
STATUS_CHOICES = (
    (STATUS_ACTIVE, STATUS_ACTIVE),
    (STATUS_NOT_STARTED, STATUS_NOT_STARTED),
    (STATUS_TERMINATED, STATUS_TERMINATED),
)
class Employee(models.Model):
    org = models.ForeignKey(
        'employee.Organization', related_name='employees',
        on_delete=models.CASCADE,
    )
    department = models.ForeignKey(
        'employee.Department', related_name='department_employees',
        on_delete=models.SET_NULL, null=True
    )
    position = models.ForeignKey(
        'employee.Position', related_name='position_employees',
        on_delete=models.SET_NULL, null=True
    )
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = models.IntegerField()
    location = models.CharField(max_length=10)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default=STATUS_ACTIVE)


class Department(models.Model):
    name = models.CharField(max_length=255)
    
    
class Position(models.Model):
    name = models.CharField(max_length=255)
    
    
class Organization(models.Model):
    name = models.CharField(max_length=255)
