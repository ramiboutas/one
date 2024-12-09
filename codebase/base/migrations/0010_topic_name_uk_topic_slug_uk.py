# Generated by Django 5.1.4 on 2024-12-09 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0009_remove_topic_name_uk_remove_topic_slug_uk"),
    ]

    operations = [
        migrations.AddField(
            model_name="topic",
            name="name_uk",
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name="topic",
            name="slug_uk",
            field=models.SlugField(blank=True, max_length=32, null=True, unique=True),
        ),
    ]
