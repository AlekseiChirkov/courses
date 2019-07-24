import json
import random
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.response import Response
from courses.models import *
from courses.serializers import *

class ContactTestCase(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            name='Name',
            description='description',
            logo='logo.jpg'
        )
        self.contacts = Contact.objects.create(
            type='PHONE',
            value='+996559129557',
            course=self.course
        )

    def test_contact(self):
        get_contact = Contact.objects.get(
            type='PHONE',
            value='+996559129557',
            course=self.course
        )
        self.assertEqual(get_contact, self.contacts)

    def test_code_status(self):
        return Response(self.contacts, status=status.HTTP_201_CREATED)

class BranchTestCase(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            name='Name',
            description='description',
            logo='logo'
        )
        self.branches = Branch.objects.create(
            address='Moskow st.',
            latitude=14.1212,
            longitude=2.5678,
            course = self.course
        )

    def test_branch(self):
        get_branch = Branch.objects.get(
            address='Moskow st.',
            latitude=14.1212,
            longitude=2.5678,
            course=self.course
        )
        self.assertEqual(get_branch, self.branches)

    def test_code_status(self):
        return Response(self.branches, status=status.HTTP_201_CREATED)

class CourseTestCase(TestCase):
    def setUp(self):
        self.courses = Course.objects.create(
            name='Name',
            description='description',
            logo='logo'
        )

    def test_course(self):
        get_course = Course.objects.get(
            name='Name',
            description='description',
            logo='logo'
        )

    def test_code_status(self):
        return Response(self.courses, status=status.HTTP_201_CREATED)
