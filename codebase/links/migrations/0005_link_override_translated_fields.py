# Generated by Django 5.1.3 on 2024-11-24 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("links", "0004_link_custom_title_el_link_custom_title_eo_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="link",
            name="override_translated_fields",
            field=models.BooleanField(default=False),
        ),
    ]
