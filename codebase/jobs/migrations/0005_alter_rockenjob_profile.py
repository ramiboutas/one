# Generated by Django 4.2.5 on 2023-09-13 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("jobs", "0004_alter_rockenjob_vacancy_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rockenjob",
            name="profile",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="jobs.profile",
            ),
        ),
    ]
