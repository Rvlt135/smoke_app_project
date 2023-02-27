import io

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import Strain


class StrainListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Strain
        fields = ('name', 'slug', 'category')


"""
class StrainListSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=250)
    slug = serializers.SlugField()
    description = serializers.CharField(read_only=True)
    created = serializers.DateTimeField(read_only=True)
    category = serializers.CharField(read_only=True)
    flavors = serializers.CharField(read_only=True)

    def create(self, validated_data):
        return Strain.objects.create(**validated_data)

    def update(self, instance, validated_data):
        #instance.id = validated_data.get("id", instance.id)
        instance.name = validated_data.get("name", instance.name)
        instance.slug = validated_data.get("slug", instance.slug)
        instance.description = validated_data.get("description", instance.description)
        instance.created = validated_data.get("created", instance.created)
        instance.category = validated_data.get("category", instance.category)
        instance.flavors = validated_data.get("flavors", instance.flavors)
        return instance

"""

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
