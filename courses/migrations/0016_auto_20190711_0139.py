# Generated by Django 2.1.7 on 2019-07-10 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_auto_20190711_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branches',
            name='latitude',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='branches',
            name='longitude',
            field=models.CharField(default='', max_length=20),
        ),
    ]