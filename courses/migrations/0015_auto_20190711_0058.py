# Generated by Django 2.1.7 on 2019-07-10 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_contacts_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branches',
            name='cours',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='courses.Courses'),
        ),
        migrations.AlterField(
            model_name='branches',
            name='latitude',
            field=models.DecimalField(decimal_places=5, max_digits=16),
        ),
        migrations.AlterField(
            model_name='branches',
            name='longitude',
            field=models.DecimalField(decimal_places=5, max_digits=16),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='cours',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='courses.Courses'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='type',
            field=models.CharField(choices=[('PHONE', 'PHONE'), ('FACEBOOK', 'FACEBOOK'), ('EMAIL', 'EMAIL')], default='', max_length=12),
        ),
        migrations.AlterField(
            model_name='courses',
            name='logo',
            field=models.CharField(max_length=128),
        ),
    ]