from django.shortcuts import render
from rest_framework import generics
from django.forms import model_to_dict
from rest_framework.views import APIView
from .models import Strain
from .serializers import StrainListSerializer
from rest_framework.response import Response


class StrainListAPIView(APIView):
    """Get object strains and list nodes with list Strain model"""
    def get(self, request):
        list_strain = Strain.objects.all()
        return Response({'srains': {'nodes':
                                        StrainListSerializer(list_strain, many=True).data}})

    """post принимает несколько параметров в body, проверяем обязательные поля из StrainListSerializer"""
    def post(self, request):
        serializer = StrainListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post_new = Strain.objects.create(name=request.data['name'],
                                         slug=request.data['slug'],
                                         description=request.data['description']
                                         )
        return Response({'post': StrainListSerializer(post_new).data})
