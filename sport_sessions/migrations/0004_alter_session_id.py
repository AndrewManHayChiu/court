# Generated by Django 5.0 on 2023-12-28 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport_sessions', '0003_session_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
