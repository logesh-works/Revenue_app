# Generated by Django 5.0 on 2023-12-27 19:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "students",
            "0007_student_age_student_community_student_date_of_birth_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="age",
            field=models.IntegerField(blank=True, default=0, verbose_name="Age"),
        ),
    ]
