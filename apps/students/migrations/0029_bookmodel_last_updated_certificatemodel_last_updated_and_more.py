# Generated by Django 5.0 on 2023-12-28 19:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("students", "0028_alter_bookmodel_received_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="bookmodel",
            name="last_updated",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="certificatemodel",
            name="last_updated",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="classmodel",
            name="last_updated",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="exammodel",
            name="last_updated",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="student",
            name="last_updated",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
