# Generated by Django 5.0.2 on 2024-02-28 22:00

import markdownx.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("content", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="menulistitem",
            name="title_en",
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name="page",
            name="body_en",
            field=markdownx.models.MarkdownxField(null=True),
        ),
        migrations.AddField(
            model_name="page",
            name="description_en",
            field=models.CharField(max_length=180, null=True),
        ),
        migrations.AddField(
            model_name="page",
            name="slug_en",
            field=models.SlugField(
                editable=False, max_length=128, null=True, unique=True
            ),
        ),
        migrations.AddField(
            model_name="page",
            name="title_en",
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name="topic",
            name="name_en",
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name="topic",
            name="slug_en",
            field=models.SlugField(max_length=32, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="article",
            name="language",
            field=models.CharField(
                choices=[
                    ("en-GB", "English GB"),
                    ("en", "English"),
                    ("es", "Spanish"),
                    ("de", "German"),
                ],
                default="en",
                max_length=8,
            ),
        ),
        migrations.AlterField(
            model_name="home",
            name="language",
            field=models.CharField(
                choices=[
                    ("en-GB", "English GB"),
                    ("en", "English"),
                    ("es", "Spanish"),
                    ("de", "German"),
                ],
                default="en",
                max_length=8,
            ),
        ),
        migrations.AlterField(
            model_name="productpage",
            name="language",
            field=models.CharField(
                choices=[
                    ("en-GB", "English GB"),
                    ("en", "English"),
                    ("es", "Spanish"),
                    ("de", "German"),
                ],
                default="en",
                max_length=8,
            ),
        ),
    ]