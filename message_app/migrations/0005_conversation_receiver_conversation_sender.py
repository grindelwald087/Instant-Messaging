# Generated by Django 4.2.16 on 2024-10-05 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message_app', '0004_remove_conversation_receiver_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='receiver',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='conversation',
            name='sender',
            field=models.CharField(max_length=50, null=True),
        ),
    ]