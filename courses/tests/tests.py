import json
import random
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import APIClient
from courses.models import *
from courses.serializers import *

client = Client()

class CategoryTestCase(TestCase):
    def setUp(self):
        pass

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

class SerializerTestCase(TestCase):
    def setUp(self):
        self.types = ['PHONE', 'FACEBOOK', 'EMAIL']
        self.values = ['+996559129557', '@example', 'example@example.com']
        self.value = random.randint(0, len(self.values))
        self.contact = 1
        self.val = self.values[self.value - 1]
        self.type = self.types[self.value - 1]
        self.category = 1
        self.id = None
        self.latitude = '14.1212'
        self.longitude = '2.5678'
        self.address = 'Moskow st.'
        self.name = 'English'
        self.description = 'Description'
        self.logo = 'logo'

        name = self.name
        description = self.description
        logo = self.logo

        self.course = Course.objects.create(
            name=name,
            description=description,
            logo=logo
        )

    def test_contact_serializer(self):
        values = {
            'type': self.type,
            'value': self.value
        }
        contact = Contact(type=self.type, value=self.value)
        serializer = ContactSerializer(contact)
        self.assertEqual(values, serializer.data)

    def test_branch_serializer(self):
        values = {
            'id': self.id,
            'address': self.address,
            'latitude': self.latitude,
            'longitude': self.longitude
            }
        branch = Branch(
            course=self.course,
            address=self.address,
            latitude=self.latitude,
            longitude=self.longitude
            )
        serializer = BranchSerializer(branch)
        self.assertEqual(values, serializer.data)

    def test_courses(self):
        values = {
            "id": None,
            'category': [],
            'name': self.name,
            'description': self.description,
            'logo': self.logo,
            'contacts': [],
            'branches': [],

        }
        print(values)
        course = Course(
            name=self.name,
            description=self.description,
            logo=self.logo)
        serializer = CourseSerializer(course)
        self.assertEqual(values, serializer.data)



# class CategoryTestCase(TestCase):
#     def setUp(self):
#         self.category = Category.objects.create(
#             name="English",
#             imgpath="https://www.google.com"
#             )
#
#     def test_category_imgpath(self):
#         english = Category.objects.get(name="English")
#         self.assertEqual(english.imgpath, 'https://www.google.com')
#
# class BranchTestCase(TestCase):
#     def course(name='English', description='description', category='category', logo='logo'):
#         return Course.objects.create(name=name)
#
#     def setUp(self):
#         self.branch = Branch.objects.create(
#             course=self.course(),
#             latitude='latitude',
#             longitude='longitude',
#             address='address'
#         )
#
#     def test_branch(self):
#         branch = Branch.objects.get(name='Branch')
#         self.assertEqual(branch.address, 'address')
#
# class CourseTestCase(TestCase):
#     def create_category(name="ExampleName", imgpath="ImgPath"):
#         return Category.objects.create(name=name, imgpath=imgpath)
#
#     def setUp(self):
#         Course.objects.create(
#             name='English',
#             description='Language course',
#             category_id=self.create_category().id,
#             logo='Logo'
#         )
#
#     def test_course_category(self):
#         english = Course.objects.get(name='English')
#         self.assertEqual(english.category_id, 1)
#
# class ContactTestCase(TestCase):
#     def create_contact(course='English', type='Phone', value='Value'):
#         return Contact.objects.create(course=course, type=type, value=vlaue)
#
#     def setUp(self):
#         Contact.objects.create(
#             course='English',
#             type='Phone',
#             value='Value'
#         )
#
#     def test_contact(self):
#         contact = Contact,objects.get(course='English')
#         self.assertEqual(contact.type, 'Phone')
