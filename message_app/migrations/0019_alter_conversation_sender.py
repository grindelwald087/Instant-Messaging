# Generated by Django 5.1.2 on 2024-11-10 05:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message_app', '0018_rename_id_fk_conversation_message_id_fk_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='message_app.users', to_field='username'),
        ),
    ]