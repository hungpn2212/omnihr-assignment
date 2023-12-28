from rest_framework import serializers
from auth.models import Organization
from employee.models import Employee


class OrgInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('id', 'name')
    


class EmployeeSerializer(serializers.ModelSerializer):
    org = OrgInfoSerializer(source='*')
    
    class Meta:
        model = Employee
        fields = '__all__'
