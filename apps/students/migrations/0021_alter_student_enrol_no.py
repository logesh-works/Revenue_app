# Generated by Django 5.0 on 2023-12-28 13:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("students", "0020_exammodel"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="enrol_no",
            field=models.CharField(max_length=8, unique=True),
        ),
    ]
