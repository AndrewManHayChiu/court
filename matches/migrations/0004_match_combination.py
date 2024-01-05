# Generated by Django 4.2 on 2024-01-05 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0003_rename_winner_score_set_team_one_score_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='combination',
            field=models.CharField(choices=[('MS', 'Mens Singles'), ('WS', 'Womens Singles'), ('MD', 'Mens Doubles'), ('WD', 'Womens Doubles'), ('XD', 'Mixed Doubles')], default='MD', max_length=2),
        ),
    ]
