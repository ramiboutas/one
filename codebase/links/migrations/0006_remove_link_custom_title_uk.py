# Generated by Django 5.1.4 on 2024-12-09 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("links", "0005_remove_link_custom_title_pt_br"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="link",
            name="custom_title_uk",
        ),
    ]
