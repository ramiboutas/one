# Generated by Django 5.1.3 on 2024-11-23 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("faqs", "0003_faq_is_active"),
    ]

    operations = [
        migrations.AddField(
            model_name="faq",
            name="answer_fr",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="question_fr",
            field=models.CharField(max_length=256, null=True),
        ),
    ]
