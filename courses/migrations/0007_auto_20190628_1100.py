# Generated by Django 2.1.7 on 2019-06-28 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20190628_1049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacts',
            old_name='type',
            new_name='name',
        ),
    ]
