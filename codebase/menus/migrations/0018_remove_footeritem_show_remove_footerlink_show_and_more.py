# Generated by Django 5.1.2 on 2024-11-03 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("menus", "0017_footerlink_show_type_navbarlink_show_type"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="footeritem",
            name="show",
        ),
        migrations.RemoveField(
            model_name="footerlink",
            name="show",
        ),
        migrations.RemoveField(
            model_name="navbarlink",
            name="show",
        ),
        migrations.RemoveField(
            model_name="socialmedialink",
            name="show",
        ),
        migrations.AddField(
            model_name="footeritem",
            name="show_type",
            field=models.CharField(
                choices=[
                    ("user", "👤 Show if user is authenticated"),
                    ("no_user", "🕵🏻 Show if user is not authenticated"),
                    ("always", "👁️ Show always"),
                    ("never", "🫣 Never show"),
                ],
                default="always",
                max_length=16,
            ),
        ),
        migrations.AddField(
            model_name="socialmedialink",
            name="show_type",
            field=models.CharField(
                choices=[
                    ("user", "👤 Show if user is authenticated"),
                    ("no_user", "🕵🏻 Show if user is not authenticated"),
                    ("always", "👁️ Show always"),
                    ("never", "🫣 Never show"),
                ],
                default="always",
                max_length=16,
            ),
        ),
        migrations.AlterField(
            model_name="footerlink",
            name="show_type",
            field=models.CharField(
                choices=[
                    ("user", "👤 Show if user is authenticated"),
                    ("no_user", "🕵🏻 Show if user is not authenticated"),
                    ("always", "👁️ Show always"),
                    ("never", "🫣 Never show"),
                ],
                default="always",
                max_length=16,
            ),
        ),
        migrations.AlterField(
            model_name="navbarlink",
            name="show_type",
            field=models.CharField(
                choices=[
                    ("user", "👤 Show if user is authenticated"),
                    ("no_user", "🕵🏻 Show if user is not authenticated"),
                    ("always", "👁️ Show always"),
                    ("never", "🫣 Never show"),
                ],
                default="always",
                max_length=16,
            ),
        ),
    ]
