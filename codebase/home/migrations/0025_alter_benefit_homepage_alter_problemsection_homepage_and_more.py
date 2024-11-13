# Generated by Django 5.1.3 on 2024-11-13 03:04

import auto_prefetch
import django.db.models.deletion
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0024_alter_herosection_cta_link_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="benefit",
            name="homepage",
            field=auto_prefetch.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="home.homepage"
            ),
        ),
        migrations.AlterField(
            model_name="problemsection",
            name="homepage",
            field=auto_prefetch.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="home.homepage"
            ),
        ),
        migrations.AlterField(
            model_name="solutionsection",
            name="homepage",
            field=auto_prefetch.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="home.homepage"
            ),
        ),
        migrations.AlterField(
            model_name="stepaction",
            name="homepage",
            field=auto_prefetch.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="home.homepage"
            ),
        ),
    ]
