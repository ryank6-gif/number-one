# Generated by Django 5.1.1 on 2024-10-02 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_remove_booking_is_completed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('noShow', 'No Show'), ('cancelled', 'Cancelled'), ('confirmed', 'Confirmed'), ('completed', 'Completed'), ('pending', 'Pending')], default='pending', max_length=20),
        ),
    ]