from rest_framework import serializers

from .models import results

class ResSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = results
        fields = '__all__'

        