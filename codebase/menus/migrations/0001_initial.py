# Generated by Django 5.1.3 on 2024-11-16 18:07

import auto_prefetch
import django.core.validators
import django.db.models.deletion
import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("links", "0001_initial"),
        ("sites", "0002_alter_domain_unique"),
    ]

    operations = [
        migrations.CreateModel(
            name="FooterItem",
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
                    "order",
                    models.PositiveSmallIntegerField(
                        default=0,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(8),
                        ],
                    ),
                ),
                ("emoji", models.CharField(blank=True, max_length=8, null=True)),
                ("title", models.CharField(max_length=64)),
                ("title_en", models.CharField(max_length=64, null=True)),
                ("title_de", models.CharField(max_length=64, null=True)),
                ("title_es", models.CharField(max_length=64, null=True)),
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
                ("site", models.ManyToManyField(to="sites.site")),
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
            name="FooterLink",
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
                    "order",
                    models.PositiveSmallIntegerField(
                        default=0,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(10),
                        ],
                    ),
                ),
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
                ("new_tab", models.BooleanField(default=False)),
                (
                    "footer_item",
                    auto_prefetch.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="menus.footeritem",
                    ),
                ),
                (
                    "link",
                    auto_prefetch.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="links.link"
                    ),
                ),
                ("site", models.ManyToManyField(to="sites.site")),
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
            name="NavbarLink",
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
                    "order",
                    models.PositiveSmallIntegerField(
                        default=0,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(10),
                        ],
                    ),
                ),
                ("emoji", models.CharField(blank=True, max_length=8, null=True)),
                ("show_as_emoji", models.BooleanField(default=False)),
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
                ("new_tab", models.BooleanField(default=False)),
                (
                    "link",
                    auto_prefetch.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="links.link"
                    ),
                ),
                ("site", models.ManyToManyField(to="sites.site")),
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
                (
                    "order",
                    models.PositiveSmallIntegerField(
                        default=0,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(10),
                        ],
                    ),
                ),
                ("url", models.URLField(max_length=256)),
                ("url_en", models.URLField(max_length=256, null=True)),
                ("url_de", models.URLField(max_length=256, null=True)),
                ("url_es", models.URLField(max_length=256, null=True)),
                ("new_tab", models.BooleanField(default=True)),
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
                ("site", models.ManyToManyField(to="sites.site")),
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