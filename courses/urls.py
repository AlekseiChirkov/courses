from django.urls import path, include
from . import views
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('course', views.CourseView)

urlpatterns = [
    path('', views.CourseView.as_view()),
]
