# Generated by Django 5.1.3 on 2024-12-07 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("faqs", "0001_initial"),
        ("sites", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="faq",
            name="sites",
            field=models.ManyToManyField(to="sites.site"),
        ),
    ]