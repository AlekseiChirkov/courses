from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import *
from .serializers import *

class ValueView(viewsets.ModelViewSet):
    queryset = Value.objects.all()
    serializer_class = ValueSerializer

class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
