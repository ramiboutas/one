# Generated by Django 5.1.3 on 2024-11-11 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("menus", "0012_remove_footerlink_allow_field_translation_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="socialmedialink",
            name="allow_field_translation",
        ),
    ]