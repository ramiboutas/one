# Generated by Django 5.1.3 on 2024-11-21 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0003_remove_articlesfolder_is_premium_article_is_premium"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="can_be_shown_in_home",
            field=models.BooleanField(default=True),
        ),
    ]
