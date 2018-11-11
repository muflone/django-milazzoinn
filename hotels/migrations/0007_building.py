# Generated by Django 2.1.3 on 2018-11-11 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0006_auto_20181111_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('floors', models.IntegerField()),
                ('address', models.TextField(blank=True)),
                ('phone1', models.CharField(blank=True, max_length=255)),
                ('phone2', models.CharField(blank=True, max_length=255)),
                ('fax', models.CharField(blank=True, max_length=255)),
                ('email', models.CharField(blank=True, max_length=255)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.Hotel')),
            ],
            options={
                'db_table': 'buildings',
            },
        ),
    ]
