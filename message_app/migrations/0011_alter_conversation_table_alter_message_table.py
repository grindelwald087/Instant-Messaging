# Generated by Django 4.2.16 on 2024-10-08 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message_app', '0010_alter_users_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='conversation',
            table='conversation',
        ),
        migrations.AlterModelTable(
            name='message',
            table='message',
        ),
    ]
