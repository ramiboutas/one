# Generated by Django 4.2.5 on 2023-09-14 10:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("jobs", "0010_alter_profile_phone_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="rockenjobsearch",
            name="name",
            field=models.CharField(default="Dummy name", max_length=32),
            preserve_default=False,
        ),
    ]
