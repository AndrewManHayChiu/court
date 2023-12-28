# Generated by Django 4.1.7 on 2023-12-26 04:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clubs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.TimeField(default='20:00')),
                ('end_time', models.TimeField(default='22:00')),
                ('doubles', models.BooleanField(default=True)),
                ('singles', models.BooleanField(default=False)),
                ('max_attendees', models.PositiveIntegerField(blank=True, default=30, null=True)),
                ('waiting_list_enabled', models.BooleanField(default=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('hidden', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clubs.club')),
            ],
        ),
        migrations.CreateModel(
            name='SessionRSVP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_attending', models.BooleanField(default=False)),
                ('paid', models.BooleanField(default=False)),
                ('payment_method', models.CharField(choices=[('cash', 'Cash'), ('bank', 'Bank Transfer'), ('other', 'Other')], max_length=10)),
                ('non_user_name', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rsvps', to='sport_sessions.session')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('session', 'user')},
            },
        ),
    ]