# Generated by Django 5.1.3 on 2024-11-27 21:27

import auto_prefetch
import django.db.models.deletion
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0010_remove_article_allow_translation_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="submodule",
            field=auto_prefetch.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="articles.articlesfolder",
            ),
            preserve_default=False,
        ),
    ]
