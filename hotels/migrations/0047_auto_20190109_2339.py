# Generated by Django 2.1.4 on 2019-01-09 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0046_structure_automatic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomtype',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
