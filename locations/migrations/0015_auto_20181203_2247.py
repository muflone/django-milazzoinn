# Generated by Django 2.1.3 on 2018-12-03 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0014_auto_20181202_2041'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='location',
            unique_together={('region', 'name')},
        ),
    ]
