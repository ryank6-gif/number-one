# Generated by Django 5.1.1 on 2024-10-02 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_alter_booking_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='is_confirmed',
        ),
    ]
