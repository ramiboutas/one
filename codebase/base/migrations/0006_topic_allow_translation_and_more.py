# Generated by Django 5.1.3 on 2024-12-09 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0005_topic_name_de_topic_name_el_topic_name_en_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="topic",
            name="allow_translation",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="topic",
            name="override_translated_fields",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="topic",
            name="slug",
            field=models.SlugField(blank=True, max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name="topic",
            name="slug_de",
            field=models.SlugField(blank=True, max_length=32, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="topic",
            name="slug_el",
            field=models.SlugField(blank=True, max_length=32, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="topic",
            name="slug_en",
            field=models.SlugField(blank=True, max_length=32, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="topic",
            name="slug_eo",
            field=models.SlugField(blank=True, max_length=32, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="topic",
            name="slug_es",
            field=models.SlugField(blank=True, max_length=32, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="topic",
            name="slug_fi",
            field=models.SlugField(blank=True, max_length=32, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="topic",
            name="slug_fr",
            field=models.SlugField(blank=True, max_length=32, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="topic",
            name="slug_it",
            field=models.SlugField(blank=True, max_length=32, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="topic",
            name="slug_nl",
            field=models.SlugField(blank=True, max_length=32, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="topic",
            name="slug_nn",
            field=models.SlugField(blank=True, max_length=32, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="topic",
            name="slug_pl",
            field=models.SlugField(blank=True, max_length=32, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="topic",
            name="slug_pt",
            field=models.SlugField(blank=True, max_length=32, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="topic",
            name="slug_pt_br",
            field=models.SlugField(blank=True, max_length=32, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="topic",
            name="slug_ru",
            field=models.SlugField(blank=True, max_length=32, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="topic",
            name="slug_sk",
            field=models.SlugField(blank=True, max_length=32, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="topic",
            name="slug_sl",
            field=models.SlugField(blank=True, max_length=32, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="topic",
            name="slug_sq",
            field=models.SlugField(blank=True, max_length=32, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="topic",
            name="slug_sr",
            field=models.SlugField(blank=True, max_length=32, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="topic",
            name="slug_sv",
            field=models.SlugField(blank=True, max_length=32, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="topic",
            name="slug_tr",
            field=models.SlugField(blank=True, max_length=32, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="topic",
            name="slug_uk",
            field=models.SlugField(blank=True, max_length=32, null=True, unique=True),
        ),
    ]
