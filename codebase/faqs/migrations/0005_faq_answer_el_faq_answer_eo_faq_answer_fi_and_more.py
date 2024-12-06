# Generated by Django 5.1.3 on 2024-11-23 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("faqs", "0004_faq_answer_fr_faq_question_fr"),
    ]

    operations = [
        migrations.AddField(
            model_name="faq",
            name="answer_el",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="answer_eo",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="answer_fi",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="answer_it",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="answer_nl",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="answer_nn",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="answer_pl",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="answer_pt",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="answer_pt_br",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="answer_ru",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="answer_sk",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="answer_sl",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="answer_sq",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="answer_sr",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="answer_sv",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="answer_tr",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="answer_uk",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="question_el",
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="question_eo",
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="question_fi",
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="question_it",
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="question_nl",
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="question_nn",
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="question_pl",
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="question_pt",
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="question_pt_br",
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="question_ru",
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="question_sk",
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="question_sl",
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="question_sq",
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="question_sr",
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="question_sv",
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="question_tr",
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="question_uk",
            field=models.CharField(max_length=256, null=True),
        ),
    ]
