# Generated by Django 5.1.3 on 2024-12-07 22:36

import auto_prefetch
import django.db.models.deletion
from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("base", "0001_initial"),
        ("sites", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="traffic",
            name="site",
            field=auto_prefetch.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to="sites.site"
            ),
        ),
    ]
