# Generated by Django 4.2.16 on 2024-10-06 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message_app', '0008_users_created_at_users_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]