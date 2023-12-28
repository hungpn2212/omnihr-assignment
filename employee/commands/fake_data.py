from typing import Any
from django.core.management import BaseCommand
from django.core.management.base import CommandParser
from faker import Faker
from auth.models import Organization
from employee.models import Employee


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
    
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            '-o',
            '--org_id',
            type=int,
            required=True,
        )
        parser.add_argument(
            '-t',
            '--total',
            type=int,
            help='total number of employee to create',
            default=10000,
        )
        
    def handle(self, *args: Any, **options: Any) -> str | None:
        org_id = options['org_id']
        total = options['total']
        
        try:
            org = Organization.objects.get(id=org_id)
        except:
            self.stderr.write('This org id does not exist')
        
        objs = []
        for _ in total:
            objs.append(Employee(
                dict(
                    first_name=self.faker.first_name(),
                    last_name=self.faker.last_name(),
                    email=self.faker.email,
                    phone_number=self.faker.phone_number(),
                    department=self.faker.word(),
                    position=self.faker.word(),
                    location=self.faker.word(),
                    org=org,
                )
            ))
        
        Employee.objects.bulk_create(objs, batch_size=10000)
        