# Generated by Django 5.1.3 on 2024-12-07 22:36

import auto_prefetch
import django.db.models.deletion
from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("home", "0001_initial"),
        ("links", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="herosection",
            name="cta_link",
            field=auto_prefetch.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="links.link"
            ),
        ),
    ]
