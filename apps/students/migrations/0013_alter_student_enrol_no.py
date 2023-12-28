# Generated by Django 5.0 on 2023-12-28 05:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("students", "0012_alter_student_community_alter_student_passport_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="enrol_no",
            field=models.IntegerField(
                default=0, unique=True, verbose_name="Enrollment Number"
            ),
        ),
    ]
