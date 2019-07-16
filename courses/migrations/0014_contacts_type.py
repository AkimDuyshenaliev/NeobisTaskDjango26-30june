# Generated by Django 2.1.7 on 2019-06-28 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_auto_20190628_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='type',
            field=models.CharField(choices=[('ph', 'PHONE'), ('fc', 'FACEBOOK'), ('em', 'EMAIL')], default='', max_length=2),
        ),
    ]