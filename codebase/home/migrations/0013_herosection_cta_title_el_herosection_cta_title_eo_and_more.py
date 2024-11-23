# Generated by Django 5.1.3 on 2024-11-23 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0012_herosection_cta_title_fr_herosection_headline_fr_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="herosection",
            name="cta_title_el",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="cta_title_eo",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="cta_title_fi",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="cta_title_it",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="cta_title_nl",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="cta_title_nn",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="cta_title_pl",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="cta_title_pt",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="cta_title_pt_br",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="cta_title_ru",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="cta_title_sk",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="cta_title_sl",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="cta_title_sq",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="cta_title_sr",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="cta_title_sv",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="cta_title_tr",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="cta_title_uk",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="headline_el",
            field=models.TextField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="headline_eo",
            field=models.TextField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="headline_fi",
            field=models.TextField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="headline_it",
            field=models.TextField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="headline_nl",
            field=models.TextField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="headline_nn",
            field=models.TextField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="headline_pl",
            field=models.TextField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="headline_pt",
            field=models.TextField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="headline_pt_br",
            field=models.TextField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="headline_ru",
            field=models.TextField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="headline_sk",
            field=models.TextField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="headline_sl",
            field=models.TextField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="headline_sq",
            field=models.TextField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="headline_sr",
            field=models.TextField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="headline_sv",
            field=models.TextField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="headline_tr",
            field=models.TextField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="headline_uk",
            field=models.TextField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="subheadline_el",
            field=models.TextField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="subheadline_eo",
            field=models.TextField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="subheadline_fi",
            field=models.TextField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="subheadline_it",
            field=models.TextField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="subheadline_nl",
            field=models.TextField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="subheadline_nn",
            field=models.TextField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="subheadline_pl",
            field=models.TextField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="subheadline_pt",
            field=models.TextField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="subheadline_pt_br",
            field=models.TextField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="subheadline_ru",
            field=models.TextField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="subheadline_sk",
            field=models.TextField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="subheadline_sl",
            field=models.TextField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="subheadline_sq",
            field=models.TextField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="subheadline_sr",
            field=models.TextField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="subheadline_sv",
            field=models.TextField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="subheadline_tr",
            field=models.TextField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="herosection",
            name="subheadline_uk",
            field=models.TextField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="benefits_title_el",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="benefits_title_eo",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="benefits_title_fi",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="benefits_title_it",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="benefits_title_nl",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="benefits_title_nn",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="benefits_title_pl",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="benefits_title_pt",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="benefits_title_pt_br",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="benefits_title_ru",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="benefits_title_sk",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="benefits_title_sl",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="benefits_title_sq",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="benefits_title_sr",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="benefits_title_sv",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="benefits_title_tr",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="benefits_title_uk",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="faqs_title_el",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="faqs_title_eo",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="faqs_title_fi",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="faqs_title_it",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="faqs_title_nl",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="faqs_title_nn",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="faqs_title_pl",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="faqs_title_pt",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="faqs_title_pt_br",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="faqs_title_ru",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="faqs_title_sk",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="faqs_title_sl",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="faqs_title_sq",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="faqs_title_sr",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="faqs_title_sv",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="faqs_title_tr",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="faqs_title_uk",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="steps_title_el",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="steps_title_eo",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="steps_title_fi",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="steps_title_it",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="steps_title_nl",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="steps_title_nn",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="steps_title_pl",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="steps_title_pt",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="steps_title_pt_br",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="steps_title_ru",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="steps_title_sk",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="steps_title_sl",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="steps_title_sq",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="steps_title_sr",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="steps_title_sv",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="steps_title_tr",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="steps_title_uk",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="title_el",
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="title_eo",
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="title_fi",
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="title_it",
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="title_nl",
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="title_nn",
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="title_pl",
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="title_pt",
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="title_pt_br",
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="title_ru",
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="title_sk",
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="title_sl",
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="title_sq",
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="title_sr",
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="title_sv",
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="title_tr",
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="title_uk",
            field=models.CharField(max_length=64, null=True),
        ),
    ]
