# Generated by Django 5.0 on 2023-12-27 15:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("students", "0005_remove_student_age_remove_student_date_of_birth_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="address",
        ),
        migrations.RemoveField(
            model_name="student",
            name="email",
        ),
    ]
