# Generated by Django 3.2.25 on 2024-08-05 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_alter_usersubscription_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserSubscription',
        ),
    ]
