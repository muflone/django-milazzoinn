# Generated by Django 2.2.10 on 2020-03-05 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0063_equipment_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='pec',
            field=models.CharField(blank=True, max_length=255, verbose_name='PEC email'),
        ),
    ]
