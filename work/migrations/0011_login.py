# Generated by Django 2.1.4 on 2018-12-16 16:55

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('work', '0010_contract_optional_end_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='work.Employee')),
            ],
            options={
                'db_table': 'work_logins',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]