from unittest import TestCase

from employee.models import Employee
from employee.column_config import EmployeeColumn
from employee.serializers import EmployeeListSerializer
from employee.tests.factories import EmployeeFactory


class EmployeeListSerializerTestCase(TestCase):
    def test_serializer_with_custom_fields(self):
        custom_fields = [EmployeeColumn.FIRST_NAME, EmployeeColumn.LAST_NAME, EmployeeColumn.EMAIL]
        employee1 = EmployeeFactory()
        qs = Employee.objects.filter(org=employee1.org)
        
        serializer = EmployeeListSerializer(qs, fields=custom_fields)
        expected_data = {
            'first_name': employee1.first_name,
            'last_name': employee1.last_name,
            'email': employee1.email,
        }
        self.assertEqual(serializer.data, expected_data)
