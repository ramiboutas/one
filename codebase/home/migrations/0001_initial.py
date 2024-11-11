# Generated by Django 5.1.3 on 2024-11-10 07:25

import auto_prefetch
import codebase.utils.abstracts_and_mixins
import django.db.models.deletion
import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("articles", "0002_initial"),
        ("pages", "0001_initial"),
        ("plans", "0001_initial"),
        ("sites", "0005_delete_extendedsite"),
    ]

    operations = [
        migrations.CreateModel(
            name="HeroCTA",
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
                (
                    "external_url",
                    models.URLField(blank=True, max_length=256, null=True),
                ),
                ("new_tab", models.BooleanField(default=False)),
                (
                    "show_type",
                    models.CharField(
                        choices=[
                            ("user", "👤 For logged user"),
                            ("no_user", "🕵🏻 For anonymous user"),
                            ("always", "👁️ Show always"),
                            ("never", "🫣 Never show"),
                        ],
                        default="always",
                        max_length=16,
                    ),
                ),
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
                ("site", models.ManyToManyField(to="sites.site")),
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
            name="HomePage",
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
                ("enable_hero_testing", models.BooleanField(default=False)),
                (
                    "site",
                    auto_prefetch.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="sites.site",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "base_manager_name": "prefetch_manager",
            },
            bases=(models.Model, codebase.utils.abstracts_and_mixins.PageMixin),
            managers=[
                ("objects", django.db.models.manager.Manager()),
                ("prefetch_manager", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="Hero",
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
                ("headline", models.TextField(max_length=256)),
                ("subheadline", models.TextField(max_length=256)),
                ("image", models.ImageField(upload_to="homepages/hero/")),
                ("active", models.BooleanField()),
                (
                    "cta",
                    auto_prefetch.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="home.herocta",
                    ),
                ),
                (
                    "homepage",
                    auto_prefetch.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="home.homepage",
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