# Generated by Django 5.1.3 on 2024-11-27 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0016_homepage_number_of_last_articles"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="homepage",
            name="number_of_last_articles",
        ),
        migrations.AddField(
            model_name="homepage",
            name="num_articles",
            field=models.PositiveSmallIntegerField(
                default=6, verbose_name="Number of last articles"
            ),
        ),
    ]
