from django.test import TestCase
from courses.models import *

class CategoryTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="English",
            imgpath="https://www.google.com"
            )

    def test_category_imgpath(self):
        english = Category.objects.get(name="English")
        self.assertEqual(english.imgpath, 'https://www.google.com')

class BranchTestCase(TestCase):
    def setUp(self):
        Branch.objects.create(
            course='English',
            latitude='latitude',
            longitude='longitude',
            address='address'
        )

    def test_branch_address(self):
        english = Branch.objects.get(course=self.create_course().id)
        self.assertEqual(english.address, 'address')

class CourseTestCase(TestCase):
    def create_category(name="ExampleName", imgpath="ImgPath"):
        return Category.objects.create(name=name, imgpath=imgpath)

    def setUp(self):
        Course.objects.create(
            name='English',
            description='Language course',
            category_id=self.create_category().id,
            logo='Logo'
        )

    def test_course_category(self):
        english = Course.objects.get(name='English')
        self.assertEqual(english.category_id, 1)
