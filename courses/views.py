from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import *
from .serializers import *


class CourseView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
