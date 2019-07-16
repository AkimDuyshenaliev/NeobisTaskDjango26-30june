import json
import random
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import APIClient
from .models import *
from .serializers import *

client = Client()

class CategoryTestModule(TestCase):
    def setUp(self):
        pass

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


class CoursesTestModule(TestCase):

    def setUp(self):
        self.courses = Courses.objects.create(
            name='Name', discription='discription', logo='default.jpg'
        )

    def test_Courses(self):
        Courses_get = Courses.objects.get(
            name='Name', discription='discription', logo='default.jpg')
        self.assertEqual(Courses_get, self.courses)


class ViewsTest(TestCase):
    def test_views(self):

        client = Client()

        self.all_pages = ['', 'courses/', 'category/', 'contacts/', 'branches/']
        for self.page in self.all_pages:
            _path = 'http://127.0.0.1:8000/' + self.page
            self.response = client.get(path=_path)
            print('Response status code : ' + str(self.response.status_code))
            try:
                self.assertEqual(self.response.status_code, 200)
            except:
                print('There is something wrong, the response status is : ' + self.response.status_code)
                break

        


class SerializersTest(TestCase):

    def setUp(self):
        self.types = ['PHONE', 'FACEBOOK', 'EMAIL']
        self.values = ['+996558054593', '@someone', 'akim.duyshenaliev@gmail.com']
        self.randomValue = random.randint(0, len(self.values))
        self.contact = 1
        self.value = self.values[self.randomValue - 1]
        self.type = self.types[self.randomValue - 1]
        self.category = 1
        self.id = None

        self.latitude = '75.24462'
        self.longitude = '45.21657'
        self.address = 'That\'s a god samned address field.'

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
            'id': self.id,
            'type': self.type,
            'value': self.value
        }

        contact = Contacts(
            cours=self.course, type=self.type, value=self.value)

        serializer = ContactsSerializer(contact)

        self.assertEqual(expected_values, serializer.data)

    def test_branches_serializer(self):
        expected_values = {
            'id': self.id, 
            'address': self.address, 
            'latitude': self.latitude, 
            'longitude': self.longitude
        }

        branch = Branches(cours=self.course, address=self.address,
                          latitude=self.latitude, longitude=self.longitude)

        serializer = BranchesSerializer(branch)

        self.assertEqual(expected_values, serializer.data)

    def test_courses_and_create(self):

        expected_values = {
            "id": None,
            'category': [],
            'name': self.name,
            'discription': self.discription,
            'logo': self.logo,
            'contacts': [],
            'branches': [],

        }
        print(expected_values)

        course = Courses(name=self.name, discription=self.discription, logo=self.logo)
        serializer = CoursesSerializer(course)

        self.assertEqual(expected_values, serializer.data)