# Generated by Django 2.1.3 on 2018-11-18 23:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0009_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegionAlias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.Country')),
            ],
            options={
                'verbose_name_plural': 'Region Aliases',
                'db_table': 'locations_regions_aliases',
                'ordering': ['name'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='regionalias',
            unique_together={('name', 'country')},
        ),
    ]
