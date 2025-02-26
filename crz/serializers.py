from rest_framework import serializers

from .models import customer_kyc

class CusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = customer_kyc
        fields = '__all__'
