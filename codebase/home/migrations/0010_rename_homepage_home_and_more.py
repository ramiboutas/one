# Generated by Django 5.1.4 on 2024-12-13 19:15

import auto_prefetch
import codebase.base.utils.mixins
import django.db.models.deletion
import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0009_alter_homepage_site"),
        ("sites", "0008_alter_site_name"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="HomePage",
            new_name="Home",
        ),
        migrations.RenameField(
            model_name="benefitssection",
            old_name="homepage",
            new_name="home",
        ),
        migrations.RenameField(
            model_name="herosection",
            old_name="homepage",
            new_name="home",
        ),
        migrations.RenameField(
            model_name="problemsection",
            old_name="homepage",
            new_name="home",
        ),
        migrations.RenameField(
            model_name="solutionsection",
            old_name="homepage",
            new_name="home",
        ),
        migrations.RenameField(
            model_name="stepaction",
            old_name="homepage",
            new_name="home",
        ),
        migrations.CreateModel(
            name="UserHome",
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
                ("allow_translation", models.BooleanField(default=False)),
                ("override_translated_fields", models.BooleanField(default=False)),
                (
                    "site",
                    auto_prefetch.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="sites.site"
                    ),
                ),
            ],
            options={
                "abstract": False,
                "base_manager_name": "prefetch_manager",
            },
            bases=(models.Model, codebase.base.utils.mixins.PageMixin),
            managers=[
                ("objects", django.db.models.manager.Manager()),
                ("prefetch_manager", django.db.models.manager.Manager()),
            ],
        ),
        migrations.DeleteModel(
            name="UserHomePage",
        ),
    ]
