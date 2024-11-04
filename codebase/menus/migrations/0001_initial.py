# Generated by Django 5.1.2 on 2024-10-31 16:26

import auto_prefetch
import django.db.models.deletion
import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("articles", "0005_comment"),
        ("pages", "0002_alter_page_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="MenuItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=64)),
                ("title_en", models.CharField(max_length=64, null=True)),
                ("title_de", models.CharField(max_length=64, null=True)),
                ("title_es", models.CharField(max_length=64, null=True)),
                ("order", models.IntegerField(default=0)),
                ("show_in_navbar", models.BooleanField(default=True)),
                ("show_in_footer", models.BooleanField(default=True)),
            ],
            options={
                "ordering": ("order",),
                "abstract": False,
                "base_manager_name": "prefetch_manager",
            },
            managers=[
                ("objects", django.db.models.manager.Manager()),
                ("prefetch_manager", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="SocialMediaLink",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=128, null=True)),
                ("title_en", models.CharField(blank=True, max_length=128, null=True)),
                ("title_de", models.CharField(blank=True, max_length=128, null=True)),
                ("title_es", models.CharField(blank=True, max_length=128, null=True)),
                ("url", models.URLField(blank=True, max_length=128, null=True)),
                ("url_en", models.URLField(blank=True, max_length=128, null=True)),
                ("url_de", models.URLField(blank=True, max_length=128, null=True)),
                ("url_es", models.URLField(blank=True, max_length=128, null=True)),
                ("target_blank", models.BooleanField(default=False)),
                ("show", models.BooleanField(default=True)),
            ],
            options={
                "abstract": False,
                "base_manager_name": "prefetch_manager",
            },
            managers=[
                ("objects", django.db.models.manager.Manager()),
                ("prefetch_manager", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="PageLink",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("order", models.IntegerField(default=0)),
                ("emoji", models.CharField(blank=True, max_length=8, null=True)),
                (
                    "custom_title",
                    models.CharField(blank=True, max_length=128, null=True),
                ),
                (
                    "custom_title_en",
                    models.CharField(blank=True, max_length=128, null=True),
                ),
                (
                    "custom_title_de",
                    models.CharField(blank=True, max_length=128, null=True),
                ),
                (
                    "custom_title_es",
                    models.CharField(blank=True, max_length=128, null=True),
                ),
                ("emoji_as_title", models.BooleanField(default=False)),
                ("show_in_navbar", models.BooleanField(default=False)),
                (
                    "url_path",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("home", "Home"),
                            ("search", "Search"),
                            ("sitemap", "Sitemap"),
                            ("article-list", "Articles"),
                        ],
                        max_length=32,
                        null=True,
                    ),
                ),
                (
                    "external_url",
                    models.URLField(blank=True, max_length=128, null=True),
                ),
                ("target_blank", models.BooleanField(default=False)),
                (
                    "article",
                    auto_prefetch.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="articles.article",
                    ),
                ),
                (
                    "menu_item",
                    auto_prefetch.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="menus.menuitem",
                    ),
                ),
                (
                    "page",
                    auto_prefetch.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pages.page",
                    ),
                ),
            ],
            options={
                "ordering": ("order",),
                "abstract": False,
                "base_manager_name": "prefetch_manager",
            },
            managers=[
                ("objects", django.db.models.manager.Manager()),
                ("prefetch_manager", django.db.models.manager.Manager()),
            ],
        ),
    ]