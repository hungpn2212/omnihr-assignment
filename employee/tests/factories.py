import factory

from employee.models import (
    Department,
    Position,
    Organization,
    Employee,
    STATUS_CHOICES,
)


class DepartmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Department
    
    name = factory.Sequence(lambda n: f'Department {n}')
    
    
class PositionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Position
    
    name = factory.Sequence(lambda n: f'Position {n}')
    
    
class OrganizationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Organization
    
    name = factory.Sequence(lambda n: f'Organization {n}')
    
    
class EmployeeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Employee
        
    org = factory.SubFactory(OrganizationFactory)
    position = factory.SubFactory(Position)
    department = factory.SubFactory(Department)
    
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    country = factory.Faker('country_code', representation='alpha-2')
    phone_number = factory.Faker('phone_number')
    email = factory.Faker('email')
    status = factory.fuzzy.FuzzyChoice(
        x[0] for x in STATUS_CHOICES
    )
