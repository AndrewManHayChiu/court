# Generated by Django 4.1.7 on 2023-12-17 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_event_created_datetime_event_deleted_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='player_limit',
            field=models.IntegerField(blank=True, default=2, null=True),
        ),
    ]
