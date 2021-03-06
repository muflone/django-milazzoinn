# Generated by Django 2.1.5 on 2019-06-02 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jsonapi', '0002_apilog_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiContextType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'api_context_types',
                'ordering': ['name'],
            },
        ),
    ]
