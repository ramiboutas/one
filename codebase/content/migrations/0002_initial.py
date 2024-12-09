# Generated by Django 5.0.2 on 2024-02-25 23:18

import auto_prefetch
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("content", "0001_initial"),
        #  ("products", "0001_initial"),
    ]

    operations = [
        # migrations.AddField(
        #     model_name="productpage",
        #     name="product",
        #     field=auto_prefetch.ForeignKey(
        #         null=True,
        #         on_delete=django.db.models.deletion.SET_NULL,
        #         to="content.listingproduct",
        #     ),
        # ),
        migrations.AddField(
            model_name="productpagefeature",
            name="product_page",
            field=auto_prefetch.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="feature_set",
                to="content.productpage",
            ),
        ),
        migrations.AddField(
            model_name="productpage",
            name="topics",
            field=models.ManyToManyField(to="content.topic"),
        ),
        migrations.AddField(
            model_name="pagelink",
            name="topic",
            field=auto_prefetch.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="content.topic",
            ),
        ),
        migrations.AddField(
            model_name="article",
            name="topic",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="content.topic",
            ),
        ),
    ]
