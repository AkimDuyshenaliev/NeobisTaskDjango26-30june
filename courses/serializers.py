from rest_framework import serializers, fields
from .models import *


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ['id', 'type', 'value']


class BranchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields = ['id', 'address', 'latitude', 'longitude']

class CoursesSerializer(serializers.ModelSerializer):
    contacts = ContactsSerializer(many=True)
    branches = BranchesSerializer(many=True)

    class Meta:
        model = Courses
        fields = ['id', 'name', 'discription',
                  'category', 'logo', 'contacts', 'branches']

    def create(self, validated_data):
        contacts_data = validated_data.pop('contacts')
        branches_data = validated_data.pop('branches')
        cours = Courses.objects.create(**validated_data)
        contacts_list = []
        branches_list = []
        for branch_data in branches_data:
            branches_list.append(Branches.objects.create(cours_id = cours.id, **branch_data))
        for contact_data in contacts_data:
            contacts_list.append(Contacts.objects.create(cours_id = cours.id, **contact_data))
        cours.save()
        return Courses
