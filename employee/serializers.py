from rest_framework import serializers
from employee.models import Employee
from employee.column_config import EmployeeColumn

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeListSerializer(serializers.ListSerializer):
    child = EmployeeSerializer
    base_fields = EmployeeColumn.get_ui_columns()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields = kwargs.get('fields') or self.base_fields
    
    def to_representation(self, data):
        return {k: v for k, v in data.items() if k in self.fields}
