# Generated by Django 4.1.5 on 2023-01-07 07:19

import core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_member_email_alter_member_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='first_name',
            field=models.CharField(max_length=100, validators=[core.validators.Validators.alphabet_validator]),
        ),
        migrations.AlterField(
            model_name='member',
            name='last_name',
            field=models.CharField(max_length=100, validators=[core.validators.Validators.alphabet_validator]),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone_number',
            field=models.CharField(max_length=100, unique=True, validators=[core.validators.Validators.phone_number_validator]),
        ),
        migrations.AlterField(
            model_name='role',
            name='role_name',
            field=models.CharField(max_length=100, validators=[core.validators.Validators.alphabet_validator]),
        ),
    ]