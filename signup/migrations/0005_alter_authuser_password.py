# Generated by Django 4.2.2 on 2023-07-04 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0004_alter_authuser_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
