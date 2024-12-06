# Generated by Django 5.1.3 on 2024-11-23 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0004_article_can_be_shown_in_home"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="body_fr",
            field=models.TextField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name="article",
            name="slug_fr",
            field=models.SlugField(
                editable=False, max_length=128, null=True, unique=True
            ),
        ),
        migrations.AddField(
            model_name="article",
            name="title_fr",
            field=models.CharField(editable=False, max_length=256, null=True),
        ),
    ]
