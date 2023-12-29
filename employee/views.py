from django.db.models import Q

from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.mixins import ListModelMixin

from employee.models import Employee
from employee.serializers import EmployeeSerializer


class EmployeePagination(LimitOffsetPagination):
    default_limit = 10


class EmployeeViewSet(ListModelMixin, viewsets.GenericViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    pagination_class = EmployeePagination
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(org_id=self.kwargs['org_id'])
    
    def filter_queryset(self, qs):
        mappings = {
            'status': 'status',
            'location': 'location',
            'department': 'department__name',
            'position': 'position__name',
        }
        
        for key, value in mappings.items():
            filter_values = self.request.query_params.getlist(key)
            if filter_values:
                qs = qs.filter(
                    Q(**{f'{value}__in': filter_values})
                )

        return qs
