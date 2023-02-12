import io

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import Strain


"""class StrainModel:
    def __init__(self, name, slug):
        self.name = name
        self.slug = slug"""


class StrainListSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=250)
    slug = serializers.SlugField()
    description = serializers.CharField(read_only=True)
    created = serializers.DateTimeField(read_only=True)
    category = serializers.CharField(read_only=True)
    flavors = serializers.CharField(read_only=True)


"""
def encode():
    model = StrainModel('asa', 'test_slug')
    model_sr = StrainSerializer(model)
    print(model_sr.data, type(model_sr.data), sep='\n')
    json = JSONRenderer().render(model_sr.data)
    print(json)


def decode():
    stream = io.BytesIO(b'{"name": "asa", "slug": "test_slug"}')
    data = JSONParser().parse(stream)
    serializer = StrainSerializer(data=data)
    serializer.is_valid()
    print(serializer.validated_data)
"""