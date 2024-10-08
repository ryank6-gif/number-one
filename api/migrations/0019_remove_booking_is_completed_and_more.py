# Generated by Django 5.1.1 on 2024-10-02 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_alter_timeoffrequest_isapproved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='is_completed',
        ),
        migrations.AlterField(
            model_name='timeoffrequest',
            name='isApproved',
            field=models.BooleanField(default=False, null=True, verbose_name='Is Approved'),
        ),
    ]
