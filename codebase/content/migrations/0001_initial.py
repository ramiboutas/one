# Generated by Django 5.0.2 on 2024-02-25 23:18

import auto_prefetch
import content.models
import django.db.models.deletion
import django.db.models.manager
import markdownx.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
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
                ("title", models.CharField(max_length=128)),
                ("description", models.CharField(max_length=180)),
                ("slug", models.SlugField(editable=False, max_length=128, unique=True)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("public", models.BooleanField(default=True)),
                ("home_listing", models.BooleanField(default=False)),
                ("published_in_medium", models.BooleanField(default=False)),
                (
                    "language",
                    models.CharField(
                        choices=[
                            ("en-GB", "English GB"),
                            ("es", "Spanish"),
                            ("de", "German"),
                        ],
                        default="en-GB",
                        max_length=8,
                    ),
                ),
                ("body", markdownx.models.MarkdownxField(null=True)),
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
            name="Home",
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
                ("title", models.CharField(max_length=128)),
                ("description", models.CharField(max_length=180)),
                ("slug", models.SlugField(editable=False, max_length=128, unique=True)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("public", models.BooleanField(default=True)),
                (
                    "language",
                    models.CharField(
                        choices=[
                            ("en-GB", "English GB"),
                            ("es", "Spanish"),
                            ("de", "German"),
                        ],
                        default="en-GB",
                        max_length=8,
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
        migrations.CreateModel(
            name="MenuListItem",
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
                ("title", models.CharField(max_length=128)),
                ("title_en_GB", models.CharField(max_length=128, null=True)),
                ("title_es", models.CharField(max_length=128, null=True)),
                ("title_de", models.CharField(max_length=128, null=True)),
                ("show_in_navbar", models.BooleanField(default=False)),
                ("order", models.IntegerField(default=0)),
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
            name="Page",
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
                ("title", models.CharField(max_length=128)),
                ("title_en_GB", models.CharField(max_length=128, null=True)),
                ("title_es", models.CharField(max_length=128, null=True)),
                ("title_de", models.CharField(max_length=128, null=True)),
                ("description", models.CharField(max_length=180)),
                ("description_en_GB", models.CharField(max_length=180, null=True)),
                ("description_es", models.CharField(max_length=180, null=True)),
                ("description_de", models.CharField(max_length=180, null=True)),
                ("slug", models.SlugField(editable=False, max_length=128, unique=True)),
                (
                    "slug_en_GB",
                    models.SlugField(
                        editable=False, max_length=128, null=True, unique=True
                    ),
                ),
                (
                    "slug_es",
                    models.SlugField(
                        editable=False, max_length=128, null=True, unique=True
                    ),
                ),
                (
                    "slug_de",
                    models.SlugField(
                        editable=False, max_length=128, null=True, unique=True
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("public", models.BooleanField(default=True)),
                ("body", markdownx.models.MarkdownxField(null=True)),
                ("body_en_GB", markdownx.models.MarkdownxField(null=True)),
                ("body_es", markdownx.models.MarkdownxField(null=True)),
                ("body_de", markdownx.models.MarkdownxField(null=True)),
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
            name="ProductPage",
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
                ("title", models.CharField(max_length=128)),
                ("description", models.CharField(max_length=180)),
                ("slug", models.SlugField(editable=False, max_length=128, unique=True)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("public", models.BooleanField(default=True)),
                ("home_listing", models.BooleanField(default=True)),
                (
                    "language",
                    models.CharField(
                        choices=[
                            ("en-GB", "English GB"),
                            ("es", "Spanish"),
                            ("de", "German"),
                        ],
                        default="en-GB",
                        max_length=8,
                    ),
                ),
                ("body", markdownx.models.MarkdownxField(blank=True, null=True)),
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
            name="ProductPageFeature",
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
                ("emoji", models.CharField(max_length=4)),
                ("title", models.CharField(max_length=64)),
                ("description", models.TextField()),
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
            name="SearchTerm",
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
                ("q", models.TextField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name="Topic",
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
                ("name", models.CharField(max_length=32)),
                ("name_en_GB", models.CharField(max_length=32, null=True)),
                ("name_es", models.CharField(max_length=32, null=True)),
                ("name_de", models.CharField(max_length=32, null=True)),
                ("slug", models.SlugField(max_length=32, unique=True)),
                ("slug_en_GB", models.SlugField(max_length=32, null=True, unique=True)),
                ("slug_es", models.SlugField(max_length=32, null=True, unique=True)),
                ("slug_de", models.SlugField(max_length=32, null=True, unique=True)),
                ("public", models.BooleanField(default=False)),
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
            name="ArticleFile",
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
                ("name", models.CharField(max_length=128, null=True)),
                (
                    "file",
                    models.FileField(upload_to=content.models.upload_article_file),
                ),
                (
                    "article",
                    auto_prefetch.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="content.article",
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
        migrations.CreateModel(
            name="ArticlesRedirect",
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
                ("slug", models.CharField(max_length=128)),
                (
                    "redirect_to",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="content.article",
                    ),
                ),
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
                (
                    "external_title",
                    models.CharField(blank=True, max_length=128, null=True),
                ),
                (
                    "external_url",
                    models.URLField(blank=True, max_length=128, null=True),
                ),
                ("target_blank", models.BooleanField(default=False)),
                (
                    "menu",
                    auto_prefetch.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="content.menulistitem",
                    ),
                ),
                (
                    "page",
                    auto_prefetch.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="content.page",
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
