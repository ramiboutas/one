# Generated by Django 5.1.3 on 2024-11-13 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0009_alter_traffic_request_get_ref"),
    ]

    operations = [
        migrations.AlterField(
            model_name="traffic",
            name="request_country_code",
            field=models.CharField(max_length=8, null=True),
        ),
    ]
