# Generated by Django 2.1.7 on 2019-06-28 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20190628_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='logo',
            field=models.CharField(max_length=80),
        ),
    ]
