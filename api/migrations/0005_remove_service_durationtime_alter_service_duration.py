# Generated by Django 5.1.1 on 2024-10-01 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_service_barberqualification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='durationTime',
        ),
        migrations.AlterField(
            model_name='service',
            name='duration',
            field=models.DurationField(help_text='Enter Service Duration in Minutes', max_length=50, verbose_name='Service Duration'),
        ),
    ]