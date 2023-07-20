# Generated by Django 4.2.2 on 2023-07-04 12:19

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0007_alter_authuser_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='authuser',
            name='phone_no',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]
