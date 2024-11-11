# Generated by Django 5.1.3 on 2024-11-11 19:57

import auto_prefetch
import django.db.models.deletion
import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("articles", "0002_initial"),
        ("pages", "0001_initial"),
        ("plans", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Link",
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
                (
                    "custom_title",
                    models.CharField(blank=True, max_length=128, null=True),
                ),
                (
                    "external_url",
                    models.URLField(blank=True, max_length=256, null=True),
                ),
                (
                    "django_url_path",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("home", "Home"),
                            ("search", "Search"),
                            ("sitemap", "Sitemap"),
                            ("article_list", "Articles"),
                            ("plan_list", "Plans"),
                            ("account_login", "Sign In"),
                            ("account_signup", "Sign Up"),
                            ("user_dashboard", "Account"),
                        ],
                        max_length=32,
                        null=True,
                    ),
                ),
                ("new_tab", models.BooleanField(default=False)),
                ("allow_field_translation", models.BooleanField(default=False)),
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
                    "page",
                    auto_prefetch.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pages.page",
                    ),
                ),
                (
                    "plan",
                    auto_prefetch.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="plans.plan",
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