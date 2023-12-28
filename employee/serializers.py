from rest_framework import serializers
from employee.models import Employee, Organization

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
