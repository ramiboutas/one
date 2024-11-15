# Generated by Django 5.1.3 on 2024-11-15 16:54

import auto_prefetch
import django.contrib.sites.models
import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("articles", "0001_initial"),
        ("pages", "__first__"),
        ("sites", "0005_delete_extendedsite"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ExtendedSite",
            fields=[
                (
                    "site_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="sites.site",
                    ),
                ),
                ("remarks", models.TextField(blank=True, null=True)),
                ("emoji", models.CharField(max_length=8, null=True)),
                ("emoji_in_brand", models.BooleanField(default=True)),
                ("default_page_title", models.CharField(max_length=64, null=True)),
                ("default_page_title_en", models.CharField(max_length=64, null=True)),
                ("default_page_title_de", models.CharField(max_length=64, null=True)),
                ("default_page_title_es", models.CharField(max_length=64, null=True)),
                (
                    "default_page_description",
                    models.TextField(max_length=256, null=True),
                ),
                (
                    "default_page_description_en",
                    models.TextField(max_length=256, null=True),
                ),
                (
                    "default_page_description_de",
                    models.TextField(max_length=256, null=True),
                ),
                (
                    "default_page_description_es",
                    models.TextField(max_length=256, null=True),
                ),
                ("default_page_keywords", models.TextField(max_length=128, null=True)),
                (
                    "default_page_keywords_en",
                    models.TextField(max_length=128, null=True),
                ),
                (
                    "default_page_keywords_de",
                    models.TextField(max_length=128, null=True),
                ),
                (
                    "default_page_keywords_es",
                    models.TextField(max_length=128, null=True),
                ),
                ("change_theme_light_in_footer", models.BooleanField(default=True)),
                ("change_theme_light_in_navbar", models.BooleanField(default=True)),
                ("change_language_in_navbar", models.BooleanField(default=True)),
                ("change_language_in_footer", models.BooleanField(default=True)),
                ("allow_field_translation", models.BooleanField(default=False)),
                ("last_huey_flush", models.DateTimeField(null=True)),
                ("has_user_home", models.BooleanField(default=False)),
                (
                    "article_folders",
                    models.ManyToManyField(
                        related_name="+", to="articles.articlesfolder"
                    ),
                ),
                (
                    "page_folders",
                    models.ManyToManyField(related_name="+", to="pages.pagesfolder"),
                ),
            ],
            bases=("sites.site",),
            managers=[
                ("objects", django.contrib.sites.models.SiteManager()),
            ],
        ),
        migrations.CreateModel(
            name="Traffic",
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
                ("request_path", models.CharField(max_length=255)),
                ("request_method", models.CharField(default="GET", max_length=7)),
                ("request_GET", models.TextField(null=True)),
                ("request_POST", models.TextField(null=True)),
                ("request_GET_ref", models.CharField(max_length=255, null=True)),
                ("request_headers", models.TextField(null=True)),
                ("request_country_code", models.CharField(max_length=8, null=True)),
                ("response_code", models.PositiveSmallIntegerField(default=200)),
                ("response_headers", models.TextField(null=True)),
                (
                    "time",
                    models.DateTimeField(
                        db_index=True,
                        default=django.utils.timezone.now,
                        verbose_name="time",
                    ),
                ),
                (
                    "request_site",
                    auto_prefetch.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="sites.site",
                    ),
                ),
                (
                    "request_user",
                    auto_prefetch.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
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
    ]
