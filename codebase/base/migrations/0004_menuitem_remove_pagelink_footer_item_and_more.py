# Generated by Django 5.1.2 on 2024-10-24 19:27

import auto_prefetch
import django.db.models.deletion
import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0003_rename_custom_title_pagelink_external_title_and_more"),
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
        migrations.RemoveField(
            model_name="pagelink",
            name="footer_item",
        ),
        migrations.RemoveField(
            model_name="pagelink",
            name="navbar_item",
        ),
        migrations.AddField(
            model_name="pagelink",
            name="menu_item",
            field=auto_prefetch.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="base.menuitem",
            ),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name="FooterItem",
        ),
        migrations.DeleteModel(
            name="NavbarItem",
        ),
    ]
