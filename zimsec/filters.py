import django_filters
from .models import results 

class ResultModelFilter(django_filters.FilterSet):
    national_id = django_filters.CharFilter(field_name='national_id', lookup_expr='icontains')

    class Meta:
        model = results
        fields = ['national_id']