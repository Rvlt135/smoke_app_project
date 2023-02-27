from django.shortcuts import render
from rest_framework import generics
from django.forms import model_to_dict
from rest_framework.views import APIView
from .models import Strain
from .serializers import StrainListSerializer
from rest_framework.response import Response


class StrainListAPIView(generics.ListCreateAPIView):
    """Get object strains and list nodes with list Strain model"""
    query_set = Strain.objects.all()
    serializer_class = Strain
    """return Response({'srains': {'nodes':
                                    StrainListSerializer(list_strain, many=True).data}})"""

    """post принимает несколько параметров в body, проверяем обязательные поля из StrainListSerializer"""
    """def post(self, request):
        serializer = StrainListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):

        serializer = StrainListSerializer(data=request.data, instance=isinstance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"put": serializer.data})

"""