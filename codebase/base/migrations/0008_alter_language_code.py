# Generated by Django 5.1.3 on 2024-11-23 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0007_language"),
    ]

    operations = [
        migrations.AlterField(
            model_name="language",
            name="code",
            field=models.CharField(db_index=True, max_length=4, unique=True),
        ),
    ]
