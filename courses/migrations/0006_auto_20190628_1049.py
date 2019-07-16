# Generated by Django 2.1.7 on 2019-06-28 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20190627_0525'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactsType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.AlterField(
            model_name='branches',
            name='latitude',
            field=models.DecimalField(decimal_places=12, max_digits=16),
        ),
        migrations.AlterField(
            model_name='branches',
            name='longitude',
            field=models.DecimalField(decimal_places=12, max_digits=16),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='type',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='courses.ContactsType'),
        ),
    ]