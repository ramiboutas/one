# Generated by Django 5.1.3 on 2024-11-11 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0013_hero_cta_new_tab"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="hero",
            name="cta",
        ),
    ]