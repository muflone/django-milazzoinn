# Generated by Django 2.1.4 on 2019-01-09 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0019_contracts'),
    ]

    operations = [
        migrations.AddField(
            model_name='activityroom',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
