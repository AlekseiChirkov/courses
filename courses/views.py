from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import *
from .serializers import *

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ContactValueView(viewsets.ModelViewSet):
    queryset = ContactValue.objects.all()
    serializer_class = ContactValueSerializer

class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
