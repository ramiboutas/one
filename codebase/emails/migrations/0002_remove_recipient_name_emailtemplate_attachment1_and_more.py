# Generated by Django 5.0.4 on 2024-04-27 08:38

import emails.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("emails", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="recipient",
            name="name",
        ),
        migrations.AddField(
            model_name="emailtemplate",
            name="attachment1",
            field=models.FileField(
                blank=True, null=True, upload_to=emails.models.upload_attachment
            ),
        ),
        migrations.AddField(
            model_name="emailtemplate",
            name="attachment2",
            field=models.FileField(
                blank=True, null=True, upload_to=emails.models.upload_attachment
            ),
        ),
        migrations.AddField(
            model_name="emailtemplate",
            name="attachment3",
            field=models.FileField(
                blank=True, null=True, upload_to=emails.models.upload_attachment
            ),
        ),
        migrations.AddField(
            model_name="recipient",
            name="draft",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="recipient",
            name="email_sent",
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name="recipient",
            name="email_sent_on",
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
    ]
