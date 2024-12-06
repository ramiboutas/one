# Generated by Django 5.1.3 on 2024-11-16 18:07

import auto_prefetch
import codebase.base.utils.mixins
import django.db.models.deletion
import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PagesFolder",
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
                ("name", models.CharField(max_length=64, unique=True)),
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
                ("title", models.CharField(editable=False, max_length=256)),
                (
                    "title_en",
                    models.CharField(editable=False, max_length=256, null=True),
                ),
                (
                    "title_de",
                    models.CharField(editable=False, max_length=256, null=True),
                ),
                (
                    "title_es",
                    models.CharField(editable=False, max_length=256, null=True),
                ),
                ("slug", models.SlugField(editable=False, max_length=128, unique=True)),
                (
                    "slug_en",
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
                (
                    "slug_es",
                    models.SlugField(
                        editable=False, max_length=128, null=True, unique=True
                    ),
                ),
                ("folder", models.CharField(editable=False, max_length=128)),
                ("subfolder", models.CharField(editable=False, max_length=256)),
                ("body", models.TextField(editable=False)),
                ("body_en", models.TextField(editable=False, null=True)),
                ("body_de", models.TextField(editable=False, null=True)),
                ("body_es", models.TextField(editable=False, null=True)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                (
                    "submodule_folder",
                    auto_prefetch.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="pages.pagesfolder",
                    ),
                ),
            ],
            options={
                "ordering": ["-created_on"],
                "abstract": False,
                "base_manager_name": "prefetch_manager",
                "unique_together": {("folder", "subfolder")},
            },
            bases=(models.Model, codebase.base.utils.mixins.PageMixin),
            managers=[
                ("objects", django.db.models.manager.Manager()),
                ("prefetch_manager", django.db.models.manager.Manager()),
            ],
        ),
    ]
