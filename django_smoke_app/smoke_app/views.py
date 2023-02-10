from django.shortcuts import render
from rest_framework import generics
from .models import Strain
from .serializers import StrainSerializer


# Create your views here.
class FindStrainAPIView(generics.ListAPIView):
    queryset = Strain.objects.all()
    serializer_class = StrainSerializer