# Generated by Django 3.2.5 on 2021-07-23 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cricket_Tournament_API', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countries_table',
            name='Period',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tournament_score_table',
            name='Lost',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tournament_score_table',
            name='Position',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tournament_score_table',
            name='Series_played',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tournament_score_table',
            name='Total_points',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tournament_score_table',
            name='Won',
            field=models.IntegerField(),
        ),
    ]
