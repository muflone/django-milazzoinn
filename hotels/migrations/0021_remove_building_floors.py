# Generated by Django 2.1.3 on 2018-11-24 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0020_auto_20181124_2358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='building',
            name='floors',
        ),
    ]