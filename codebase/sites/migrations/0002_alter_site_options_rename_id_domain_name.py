# Generated by Django 5.1.3 on 2024-12-08 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("sites", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="site",
            options={
                "base_manager_name": "prefetch_manager",
                "ordering": ["domain__name"],
                "verbose_name": "site",
                "verbose_name_plural": "sites",
            },
        ),
        migrations.RenameField(
            model_name="domain",
            old_name="id",
            new_name="name",
        ),
    ]