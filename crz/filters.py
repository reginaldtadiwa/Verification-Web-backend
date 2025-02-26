import django_filters
from .models import customer_kyc

class KycModelFilter(django_filters.FilterSet):
    national_id = django_filters.CharFilter(field_name='national_id', lookup_expr='icontains')

    class Meta:
        model = customer_kyc
        fields = ['national_id']


