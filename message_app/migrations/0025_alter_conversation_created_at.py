# Generated by Django 5.1.2 on 2024-11-16 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message_app', '0024_alter_conversation_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='created_at',
            field=models.DateField(null=True),
        ),
    ]