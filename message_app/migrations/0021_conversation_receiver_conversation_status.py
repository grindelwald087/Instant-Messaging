# Generated by Django 5.1.2 on 2024-11-13 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message_app', '0020_alter_conversation_sender'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='receiver',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='conversation',
            name='status',
            field=models.CharField(max_length=10, null=True),
        ),
    ]