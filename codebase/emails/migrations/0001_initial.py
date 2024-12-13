# Generated by Django 5.0.4 on 2024-04-27 07:09

import auto_prefetch
import django.db.models.deletion
import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="EmailTemplate",
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
                ("subject", models.CharField(max_length=128)),
                ("body", models.TextField()),
                ("respond_to", models.EmailField(blank=True, max_length=64, null=True)),
                (
                    "var1_meaning",
                    models.CharField(blank=True, max_length=64, null=True),
                ),
                (
                    "var2_meaning",
                    models.CharField(blank=True, max_length=64, null=True),
                ),
                (
                    "var3_meaning",
                    models.CharField(blank=True, max_length=64, null=True),
                ),
                (
                    "var4_meaning",
                    models.CharField(blank=True, max_length=64, null=True),
                ),
                (
                    "var5_meaning",
                    models.CharField(blank=True, max_length=64, null=True),
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
            name="Recipient",
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
                ("name", models.CharField(max_length=64)),
                ("email_address", models.EmailField(max_length=64)),
                ("var1", models.CharField(blank=True, max_length=64, null=True)),
                ("var2", models.CharField(blank=True, max_length=64, null=True)),
                ("var3", models.CharField(blank=True, max_length=64, null=True)),
                ("var4", models.CharField(blank=True, max_length=64, null=True)),
                ("var5", models.CharField(blank=True, max_length=64, null=True)),
                (
                    "email_template",
                    auto_prefetch.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="emails.emailtemplate",
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
