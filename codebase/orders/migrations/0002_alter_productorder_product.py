# Generated by Django 5.0.3 on 2024-03-16 07:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("content", "0007_remove_productpagefeature_product_page_and_more"),
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productorder",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="content.listingproduct"
            ),
        ),
    ]
