from django.db import models


class Courses(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=240)
    # logo = models.ImageField(default='default.jpg', upload_to='logos')
    logo = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=80, default='')
    imgpath = models.CharField(max_length=80, default='')
    cours = models.ForeignKey(Courses, on_delete=models.CASCADE, null=True, related_name='category', default='')

    def __str__(self):
        return self.name


class Contacts(models.Model):
    phone = 'PHONE'
    facebook = 'FACEBOOK'
    email = 'EMAIL'
    contact_choices = [
        (phone, 'PHONE'),
        (facebook, 'FACEBOOK'),
        (email, 'EMAIL')
    ]

    type = models.CharField(max_length=12, choices=contact_choices, default='')
    value = models.CharField(max_length=512)
    cours = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='contacts', default='')
    

    def __str__(self):
        return self.type


class Branches(models.Model):
    address = models.CharField(max_length=120)
    latitude = models.CharField(max_length=20, default='')
    longitude = models.CharField(max_length=20, default='')
    cours = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='branches', default='')


    
