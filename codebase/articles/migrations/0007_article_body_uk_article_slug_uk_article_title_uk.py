# Generated by Django 5.1.4 on 2024-12-09 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0006_remove_article_body_uk_remove_article_slug_uk_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="body_uk",
            field=models.TextField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name="article",
            name="slug_uk",
            field=models.SlugField(
                editable=False, max_length=128, null=True, unique=True
            ),
        ),
        migrations.AddField(
            model_name="article",
            name="title_uk",
            field=models.CharField(editable=False, max_length=256, null=True),
        ),
    ]
