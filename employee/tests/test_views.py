import factory
from rest_framework import status
from rest_framework.test import APITestCase

from employee.models import (
    STATUS_ACTIVE,
    STATUS_NOT_STARTED,
)
from employee.tests.factories import (
    OrganizationFactory,
    EmployeeFactory,
    DepartmentFactory,
    PositionFactory,
)


class EmployeeViewTestCase(APITestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.org = OrganizationFactory()
        cls.base_url = f'/api/v1/{cls.org.id}/employees'
        
    def test_list_employees(self):
        employees = EmployeeFactory.create_batch(
            2,
            org=self.org,
        )
        
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = [
            {
                'id': employee.id,
                'first_name': employee.first_name,
                'last_name': employee.last_name,
                'email': employee.email,
                'phone_number': employee.phone_number,
                'location': employee.location,
                'status': employee.status,
                'department_name': employee.department.name,
                'position_name': employee.position.name,
            } for employee in employees
        ]
        self.assertCountEqual(
            response.data['results'],
            expected_data,
        )
        
    def test_list_employees__filter_by_department(self):
        department1, department2 = DepartmentFactory.create_batch(2)
        employee1, employee2, _ = EmployeeFactory.create_batch(
            3,
            org=self.org,
            department=factory.Iterator([department1, department1, department2]),
        )
        
        query_params = {
            'department': department1.name
        }
        
        response = self.client.get(self.base_url, query_params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        ids = [item['id'] for item in response.data['results']]
        self.assertCountEqual(ids, [employee1.id, employee2.id])
        
    def test_list_employees__filter_by_position(self):
        position1, position2 = PositionFactory.create_batch(2)
        employees = EmployeeFactory.create_batch(
            3,
            org=self.org,
            position=factory.Iterator([position1, position2, position2]),
        )
        
        query_params = {
            'position': position1.name
        }
        
        response = self.client.get(self.base_url, query_params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        ids = [item['id'] for item in response.data['results']]
        self.assertEqual(ids, [employees[0].id])
        
    def test_list_employees__filter_by_status(self):
        _, employee1, employee2 = EmployeeFactory.create_batch(
            3,
            org=self.org,
            status=factory.Iterator([STATUS_NOT_STARTED, STATUS_ACTIVE, STATUS_ACTIVE]),
        )
        
        query_params = {
            'status': STATUS_ACTIVE,
        }
        
        response = self.client.get(self.base_url, query_params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        ids = [item['id'] for item in response.data['results']]
        self.assertCountEqual(ids, [employee1.id, employee2.id])
        
    def test_list_employees__filter_by_location(self):
        location1 = 'VN'
        location2 = 'US'
        
        employee1, employee2, _ = EmployeeFactory.create_batch(
            3,
            org=self.org,
            location=factory.Iterator([location1, location1, location2]),
        )
        
        query_params = {
            'location': location1,
        }
        
        response = self.client.get(self.base_url, query_params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        ids = [item['id'] for item in response.data['results']]
        self.assertCountEqual(ids, [employee1.id, employee2.id])
        
    def test_list_employees__filter_by_multiple_params(self):
        department1, department2 = DepartmentFactory.create_batch(2)
        position1, position2 = PositionFactory.create_batch(2)
        location1, location2 = 'VN', 'US'
        
        employee1, employee2 = EmployeeFactory.create_batch(
            2,
            org=self.org,
            status=factory.Iterator([STATUS_ACTIVE, STATUS_NOT_STARTED]),
            department=factory.Iterator([department1, department2]),
            position=factory.Iterator([position1, position2]),
            location=factory.Iterator([location1, location2])
        )
        
        query_params = {
            'location': location1,
            'department': department1.name,
            'position': position1.name,
            'status': STATUS_ACTIVE,
        }
        
        response = self.client.get(self.base_url, query_params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        ids = [item['id'] for item in response.data['results']]
        self.assertEqual(ids, [employee1.id])
