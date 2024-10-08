# Generated by Django 5.0.9 on 2024-09-12 18:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("subscriptions", "0004_alter_subscription_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="subscription",
            name="permissions",
            field=models.ManyToManyField(
                limit_choices_to={
                    "codename__in": ["coach", "premium", "basic", "free"],
                    "content_type__app_label": "subscriptions",
                },
                to="auth.permission",
            ),
        ),
    ]
