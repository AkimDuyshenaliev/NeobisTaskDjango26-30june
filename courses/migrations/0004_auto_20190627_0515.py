# Generated by Django 2.1.7 on 2019-06-26 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20190627_0510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='Branches',
        ),
        migrations.RemoveField(
            model_name='courses',
            name='Contacts',
        ),
    ]
