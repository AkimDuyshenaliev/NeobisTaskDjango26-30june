import json
import random
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.response import Response
from .models import *
from .serializers import *

client = Client()

class CategoryTestModule(TestCase):
    def setUp(self):
        self.course = Courses.objects.create(
            name='Name', discription='discription', logo='default.jpg')

        self.category = Category.objects.create(name='Name', imgpath='image path', cours=self.course)

    def TestCategory(self):
        Category_get = Category.objects.get(
            name='Name', imgpath='image path', cours=self.course)
        self.assertEqual(Category_get, self.category)

    def testCategoryStatusCode(self):
        return Response(self.category, status=status.HTTP_201_CREATED)


class ContactTestModule(TestCase):

    def setUp(self):
        self.course = Courses.objects.create(
            name='Name', discription='discription', logo='default.jpg')


        self.contacts = Contacts.objects.create(
            type='PHONE', value='+996558054596', cours=self.course
        )

    def test_Contact(self):
        Contact_get = Contacts.objects.get(
            type='PHONE', value='+996558054596', cours=self.course)
            
        self.assertEqual(Contact_get, self.contacts)

    def testContactsStatusCode(self):
        return Response(self.contacts, status=status.HTTP_201_CREATED)


class BranchesTestModule(TestCase):

    def setUp(self):
        self.course = Courses.objects.create(
            name='Name', discription='discription', logo='default.jpg')

        self.branches = Branches.objects.create(
            address='Brandon str', latitude=78.1868, longitude=54.1861, cours = self.course
        )

    def test_Branches(self):
        Branches_get = Branches.objects.get(
            address='Brandon str', latitude=78.1868, longitude=54.1861, cours=self.course)
        self.assertEqual(Branches_get, self.branches)

    def testBranchesStatusCode(self):
        return Response(self.branches, status=status.HTTP_201_CREATED)


class CoursesTestModule(TestCase):

    def setUp(self):
        self.courses = Courses.objects.create(
            name='Name', discription='discription', logo='default.jpg'
        )

    def test_Courses(self):
        Courses_get = Courses.objects.get(
            name='Name', discription='discription', logo='default.jpg')
        self.assertEqual(Courses_get, self.courses)

    def testCoursesStatusCode(self):
        return Response(self.courses, status=status.HTTP_201_CREATED)


class ViewsTest(TestCase):
    def test_views(self):

        client = Client()

        self.all_pages = ['', 'courses/', 'category/', 'contacts/', 'branches/']
        for self.page in self.all_pages:
            _path = 'http://127.0.0.1:8000/' + self.page
            self.url_response = client.get(path=_path)
            print('Response status code : ' + str(self.url_response.status_code))
            try:
                self.assertEqual(self.url_response.status_code, 200)
            except:
                print('There is something wrong, the response status is : ' + self.url_response.status_code)
                break

        


class SerializersTest(TestCase):

    def setUp(self):

        # self.types = ['PHONE', 'FACEBOOK', 'EMAIL']
        # self.values = ['+996558054593', '@someone', 'akim.duyshenaliev@gmail.com']
        # self.randomValue = random.randint(0, len(self.values))
        # self.type = self.types[self.randomValue - 1]
        # self.value = self.values[self.randomValue - 1]

        self.type = 'PHONE'
        self.value = '+996558054593'
        self.contact = 1
        self.category = 1
        self.id = None

        self.address = 'That\'s a god samned address field.'
        self.latitude = '75.24462'
        self.longitude = '45.21657'

        self.name = 'English sth'
        self.discription = 'That\'s a fricking discription, deal with it!'
        self.logo = 'This is suppose to be a path to the image but oh well'


        name = self.name
        discription = self.discription
        logo = self.logo

        self.course = Courses.objects.create(name=name,
                                             discription=discription, logo=logo)

    def test_contacts_serializer(self):
        expected_values = {
            'id': None,
            'type': 'PHONE',
            'value': '+996558054593'
        }

        contact = Contacts(
            cours=self.course, type=self.type, value=self.value)

        serializer = ContactsSerializer(contact)

        self.assertEqual(expected_values, serializer.data)

        self.assertEqual(serializer.status_code, 201)

    def test_branches_serializer(self):
        expected_values = {
            'id': None, 
            'address': 'That\'s a god samned address field.',
            'latitude': '75.24462',
            'longitude': '45.21657'
        }

        branch = Branches(cours=self.course, address=self.address,
                          latitude=self.latitude, longitude=self.longitude)

        serializer = BranchesSerializer(branch)

        Response(serializer.data, status=status.HTTP_201_CREATED)

    def test_courses_and_create(self):

        expected_values = {
            "id": None,
            'category': [],
            'name': 'English sth',
            'discription': 'That\'s a fricking discription, deal with it!',
            'logo': 'This is suppose to be a path to the image but oh well',
            'contacts': [],
            'branches': [],

        }
        print(expected_values)

        course = Courses(name=self.name, discription=self.discription, logo=self.logo)
        serializer = CoursesSerializer(course)

        self.assertEqual(expected_values, serializer.data)
