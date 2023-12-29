from rest_framework import serializers
from employee.models import Employee
from employee.column_config import EmployeeColumn

class EmployeeSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(max_length=255, source='department.name')
    position_name = serializers.CharField(max_length=255, source='position.name')

    class Meta:
        model = Employee
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'location',
            'status',
            'department_name',
            'position_name',
        )


class EmployeeListSerializer(serializers.ListSerializer):
    child = EmployeeSerializer()
    base_fields = EmployeeColumn.get_ui_columns()
    
    def __init__(self, *args, **kwargs):
        self.fields = kwargs.pop('fields', None)
        if not self.fields:
            self.fields = self.base_fields
        super().__init__(*args, **kwargs)
    
    def to_representation(self, data):
        data = super().to_representation(data)
        return [{k: v for k, v in item.items() if k in self.fields} for item in data]
