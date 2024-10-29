# Generated by Django 5.1.1 on 2024-10-02 18:24

import api.models.validations
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_barber_agreedmargin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barber',
            name='agreedMargin',
            field=models.PositiveIntegerField(default=60, help_text='Margin a barber earns from their earnings.', validators=[api.models.validations.validate_margin], verbose_name="Barber's Margin."),
        ),
    ]