# Generated by Django 5.1.3 on 2024-11-27 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message_app', '0031_users_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='gender',
            field=models.CharField(default='', max_length=10),
        ),
    ]