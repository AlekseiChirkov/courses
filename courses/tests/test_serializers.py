import json
from django.test import TestCase, Client
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.response import Response
from courses.serializers import *

client = Client()

class SerializersTestCase(TestCase):
    def setUp(self):
        self.id = None
        self.name = 'English'
        self.imgpath = 'Imgpath'
        self.address = 'Address'
        self.latitude = '12.3456'
        self.longitude = '21.0123'
        self.type = 'EMAIL'
        self.value = 'example@mail.ru'
        self.description = 'Descripton'
        self.logo = 'Logo'
        self.category = 1

        name = self.name
        description = self.description
        logo = self.logo


        self.course = Course.objects.create(name = name,
                                            description = description,
                                            logo = logo,)

    def test_branches_serializer(self):
        expected_val = {
            'address': 'Address',
            'latitude': '12.3456',
            'longitude': '21.0123'
        }

        branch = Branch(course=self.course, address=self.address,
                        latitude=self.latitude, longitude=self.longitude)
        serializer = BranchSerializer(branch)

        self.assertEqual(expected_val, serializer.data)

    def test_branch_serializer_code_status(self):
        branch = Branch(course=self.course, address=self.address,
                        latitude=self.latitude, longitude=self.longitude)
        serializer = BranchSerializer(branch)

        serializer_data = serializer.data
        return Response(serializer_data, status=status.HTTP_201_CREATED)

    def test_contact_serializer(self):
        expected_val = {
            'type': 'EMAIL',
            'value': 'example@mail.ru'
        }

        contact = Contact(course=self.course, type=self.type, value=self.value)
        serializer = ContactSerializer(contact)

        self.assertEqual(expected_val, serializer.data)

    def test_contact_serializer_code_status(self):
        contact = Contact(course=self.course, type=self.type, value=self.value)

        serializer = ContactSerializer(contact)

        serializer_data = serializer.data
        return Response(serializer_data, status=status.HTTP_201_CREATED)

    def test_course_create(self):
        expected_val = {
            'id': None,
            'name': 'English',
            'description': 'Descripton',
            'logo': 'Logo',
            'contacts': [],
            'branches': []
        }

        course = Course(name=self.name, description=self.description, logo=self.logo)
        serializer = CourseSerializer(course)

        self.assertEqual(expected_val, serializer.data)
