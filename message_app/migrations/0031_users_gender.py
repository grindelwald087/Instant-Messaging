# Generated by Django 5.1.3 on 2024-11-27 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message_app', '0030_alter_conversation_message_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='gender',
            field=models.CharField(default='', max_length=5),
        ),
    ]
