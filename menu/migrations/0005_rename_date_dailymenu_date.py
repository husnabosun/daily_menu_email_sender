# Generated by Django 3.2.25 on 2024-08-10 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_delete_usersubscription'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dailymenu',
            old_name='date',
            new_name='Date',
        ),
    ]
