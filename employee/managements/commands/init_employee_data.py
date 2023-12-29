from typing import Any
from django.core.management import BaseCommand
from faker import Faker
from employee.models import Department, Position, Employee, Organization
import random

class Command(BaseCommand):
    def __init__(
        self,
        stdout,
        stderr,
        no_color,
        force_color,
    ) -> None:
        super().__init__(stdout, stderr, no_color, force_color)
        self.faker = Faker()
        
    def handle(self, *args: Any, **options: Any):
        department_objs = []
        position_objs = []
        
        org = Organization({
            'name': self.faker.company(),
        })
        org.save()
        self.stdout.write('Created a fake org with id {} and name {}'.format(
            org.id, org.name,
        ))
        
        for _ in range(50):
            department_objs.append(
                Department(
                    dict(name=self.faker.department())
                )
            )
            
            position_objs.append(
                Position(
                    dict(name=self.faker.job())
                )
            )
        
        Department.objects.bulk_create(department_objs)
        Position.objects.bulk_create(position_objs)
        
        objs = []
        for _ in range(100000):
            objs.append(Employee(
                dict(
                    first_name=self.faker.first_name(),
                    last_name=self.faker.last_name(),
                    email=self.faker.email,
                    phone_number=self.faker.phone_number(),
                    department_id=random.randint(1, 50),
                    position_id=random.randint(1, 50),
                    location=self.faker.country_code(),
                    org=org,
                )
            ))
        
        Employee.objects.bulk_create(objs, batch_size=10000)