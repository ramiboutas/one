# Generated by Django 5.1.3 on 2024-11-27 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0005_page_allow_translation_and_more"),
        ("sites", "0002_alter_domain_unique"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="page",
            name="submodule_folder",
        ),
        migrations.AddField(
            model_name="page",
            name="sites",
            field=models.ManyToManyField(to="sites.site"),
        ),
    ]
