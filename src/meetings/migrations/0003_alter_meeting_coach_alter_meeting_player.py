# Generated by Django 5.1.1 on 2024-09-12 22:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("meetings", "0002_meeting_coach_meeting_player"),
        ("profiles", "0002_playerprofile_coach"),
    ]

    operations = [
        migrations.AlterField(
            model_name="meeting",
            name="coach",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="profiles.coachprofile"
            ),
        ),
        migrations.AlterField(
            model_name="meeting",
            name="player",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="profiles.playerprofile"
            ),
        ),
    ]
