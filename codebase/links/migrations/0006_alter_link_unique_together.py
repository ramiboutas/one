# Generated by Django 5.1.3 on 2024-11-13 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("links", "0005_alter_link_unique_together"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="link",
            unique_together=set(),
        ),
    ]
