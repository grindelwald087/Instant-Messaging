# Generated by Django 5.1.2 on 2024-11-03 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message_app', '0016_alter_users_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='sender',
            field=models.CharField(max_length=255, null=True),
        ),
    ]