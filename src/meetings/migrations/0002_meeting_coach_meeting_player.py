# Generated by Django 5.1.1 on 2024-09-12 22:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("meetings", "0001_initial"),
        ("profiles", "0002_playerprofile_coach"),
    ]

    operations = [
        migrations.AddField(
            model_name="meeting",
            name="coach",
            field=models.OneToOneField(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="profiles.coachprofile",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="meeting",
            name="player",
            field=models.OneToOneField(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="profiles.playerprofile",
            ),
            preserve_default=False,
        ),
    ]
