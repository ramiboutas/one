# Generated by Django 5.1.4 on 2024-12-09 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0004_remove_article_body_eo_remove_article_body_fi_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="article",
            name="body_pt_br",
        ),
        migrations.RemoveField(
            model_name="article",
            name="slug_pt_br",
        ),
        migrations.RemoveField(
            model_name="article",
            name="title_pt_br",
        ),
    ]