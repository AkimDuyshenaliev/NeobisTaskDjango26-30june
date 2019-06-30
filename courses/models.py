from django.db import models


class Courses(models.Model):
    name = models.CharField(max_length=80)
    discription = models.CharField(max_length=240)
    category = models.CharField(max_length=80, default='Category')
    # logo = models.ImageField(default='default.jpg', upload_to='logos')
    logo = models.CharField(max_length=512)

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
        return self.name



class Branches(models.Model):
    address = models.CharField(max_length=120)
    latitude = models.DecimalField(max_digits=16, decimal_places=12)
    longitude = models.DecimalField(max_digits=16, decimal_places=12)
    cours = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='branches', default='')


    
