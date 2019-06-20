# Generated by Django 2.1.5 on 2019-06-06 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0031_tabletsetting'),
        ('jsonapi', '0004_api_command_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiCommand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=True)),
                ('description', models.TextField(blank=True)),
                ('starting', models.DateTimeField(blank=True, default=None, null=True)),
                ('ending', models.DateTimeField(blank=True, default=None, null=True)),
                ('command_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jsonapi.ApiCommandType')),
                ('context_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jsonapi.ApiContextType')),
                ('tablets', models.ManyToManyField(blank=True, to='work.Tablet')),
            ],
            options={
                'db_table': 'api_commands',
                'ordering': ['id'],
            },
        ),
    ]