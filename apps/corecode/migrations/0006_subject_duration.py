# Generated by Django 5.0 on 2023-12-30 13:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("corecode", "0005_book"),
    ]

    operations = [
        migrations.AddField(
            model_name="subject",
            name="duration",
            field=models.CharField(blank=True, max_length=200),
        ),
    ]