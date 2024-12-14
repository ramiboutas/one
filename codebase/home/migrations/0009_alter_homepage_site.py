# Generated by Django 5.1.4 on 2024-12-13 18:59

import auto_prefetch
import django.db.models.deletion
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0008_herosection_cta_title_uk_herosection_headline_uk_and_more"),
        ("sites", "0008_alter_site_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homepage",
            name="site",
            field=auto_prefetch.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="sites.site"
            ),
        ),
    ]
