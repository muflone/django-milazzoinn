# Generated by Django 2.1.4 on 2019-01-06 01:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0014_activity_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityInLinesProxy',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Activities with Rooms',
                'proxy': True,
                'indexes': [],
            },
            bases=('work.activity',),
        ),
    ]
