from rest_framework import serializers, fields
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'imgpath']

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ['id', 'type', 'value']


class BranchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields = ['id', 'address', 'latitude', 'longitude']

class CoursesSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    contacts = ContactsSerializer(many=True)
    branches = BranchesSerializer(many=True)

    class Meta:
        model = Courses
        fields = ['id', 'name', 'description',
                  'category', 'logo', 'contacts', 'branches']

    def create(self, validated_data):
        contacts_data = validated_data.pop('contacts')
        categorys_data = validated_data.pop('category')
        branches_data = validated_data.pop('branches')
        cours = Courses.objects.create(**validated_data)
        contacts_list = []
        category_list = []
        branches_list = []
        for branch_data in branches_data:
            branches_list.append(Branches.objects.create(cours_id = cours.id, **branch_data))
        for category_data in categorys_data:
            category_list.append(Category.objects.create(cours_id = cours.id, **category_data))
        for contact_data in contacts_data:
            contacts_list.append(Contacts.objects.create(cours_id = cours.id, **contact_data))
        cours.save()
        return Courses

    def update(self, instance, validated_data):
        instance.contacts_data = validated_data.get('id', 'type', 'value')
        instance.categorys_data = validated_data.get('id', 'name', 'imgpath')
        instance.branches_data = validated_data.get('id', 'address', 'latitude', 'longitude')
        instance.save()
        return instance

