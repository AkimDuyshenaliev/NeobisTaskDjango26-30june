# Generated by Django 2.1.7 on 2019-06-26 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='category',
            field=models.CharField(default='Category', max_length=80),
        ),
        migrations.AddField(
            model_name='courses',
            name='logo',
            field=models.ImageField(default='default.jpg', upload_to='logos'),
        ),
    ]
