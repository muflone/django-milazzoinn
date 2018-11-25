# Generated by Django 2.1.3 on 2018-11-13 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True,
                                          serialize=False)),
                ('description', models.TextField(blank=True)),
                ('capital', models.CharField(blank=True, max_length=255)),
                ('continent', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='locations.Continent')),
                ('language1', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='country_language1',
                    to='locations.Language')),
                ('language2', models.ForeignKey(
                    blank=True,
                    null=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='country_language2',
                    to='locations.Language')),
            ],
            options={
                'verbose_name_plural': 'Countries',
                'db_table': 'locations_countries',
            },
        ),
    ]
