# Generated by Django 5.1.4 on 2024-12-19 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0002_chapter_body_de_chapter_body_el_chapter_body_en_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="chapter",
            name="display",
            field=models.BooleanField(default=False),
        ),
    ]
