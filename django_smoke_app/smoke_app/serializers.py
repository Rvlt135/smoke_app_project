from rest_framework import serializers
from .models import Strain


class StrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Strain
        fields = ('name', 'slug')