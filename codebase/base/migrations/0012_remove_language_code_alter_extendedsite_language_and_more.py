# Generated by Django 5.1.3 on 2024-11-23 21:07

import auto_prefetch
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0011_remove_language_name_extendedsite_language_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="language",
            name="code",
        ),
        migrations.AlterField(
            model_name="extendedsite",
            name="language",
            field=auto_prefetch.ForeignKey(
                default="en",
                on_delete=django.db.models.deletion.CASCADE,
                to="base.language",
            ),
        ),
        migrations.AlterField(
            model_name="language",
            name="id",
            field=models.CharField(
                db_index=True, max_length=8, primary_key=True, serialize=False
            ),
        ),
    ]
