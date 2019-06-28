from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

class CoursesView(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer


class ContactsView(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


class BranchesView(viewsets.ModelViewSet):
    queryset = Branches.objects.all()
    serializer_class = BranchesSerializer
