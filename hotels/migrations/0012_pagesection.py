# Generated by Django 2.1.3 on 2018-11-11 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0011_roletype'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageSection',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True)),
                ('link', models.CharField(blank=True, max_length=255)),
                ('header_title', models.CharField(blank=True, max_length=255)),
                ('header_order', models.IntegerField()),
                ('home_title', models.CharField(blank=True, max_length=255)),
                ('home_order', models.IntegerField()),
                ('home_image', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'db_table': 'page_sections',
            },
        ),
    ]
