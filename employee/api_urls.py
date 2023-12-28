from django.url import path

from employee.views import EmployeeViewSet

url_patterns = [
    path(
        'v1/<int:org_id>/employees',
        EmployeeViewSet.as_view({
            'get': EmployeeViewSet.list.__name__,
        }),
        name='list-employees',
    )
]