# Generated by Django 5.1.3 on 2024-11-23 21:04

import auto_prefetch
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0010_rename_languges_extendedsite_languages"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="language",
            name="name",
        ),
        migrations.AddField(
            model_name="extendedsite",
            name="language",
            field=auto_prefetch.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="base.language",
            ),
        ),
        migrations.AlterField(
            model_name="extendedsite",
            name="languages",
            field=models.ManyToManyField(related_name="+", to="base.language"),
        ),
        migrations.AlterField(
            model_name="language",
            name="code",
            field=models.CharField(db_index=True, max_length=8, unique=True),
        ),
    ]
