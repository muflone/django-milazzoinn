# Generated by Django 2.1.5 on 2019-01-19 22:19

from django.db import migrations, models


def inizialize_directions(apps, schema_editor):
    TimestampDirection = apps.get_model('work', 'TimestampDirection')
    TimestampDirection.objects.create(name='Enter',
                                      description='',
                                      type_enter=True,
                                      type_exit=False)
    TimestampDirection.objects.create(name='Exit',
                                      description='',
                                      type_enter=False,
                                      type_exit=True)


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0023_employee_bank_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimestampDirection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True)),
                ('type_enter', models.BooleanField()),
                ('type_exit', models.BooleanField()),
            ],
            options={
                'db_table': 'work_timestamp_directions',
                'ordering': ['name'],
            },
        ),
        migrations.RunPython(inizialize_directions,
                             reverse_code=migrations.RunPython.noop),
    ]