# Generated by Django 5.0 on 2023-12-27 18:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("students", "0006_remove_student_address_remove_student_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="rel_occupation",
            field=models.CharField(
                default="", max_length=255, verbose_name="Father/Husband Occupation"
            ),
        ),
    ]
