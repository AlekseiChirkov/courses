from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('course', views.CourseView)
router.register('values', views.ValueView)

urlpatterns = [
    path('', include(router.urls)),
]
