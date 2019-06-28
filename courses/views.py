from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import *
from .serializers import *

class ContactValueView(viewsets.ModelViewSet):
    queryset = ContactValue.objects.all()
    serializer_class = ContactValueSerializer

class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
