# Generated by Django 5.0 on 2023-12-30 09:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("course", "0001_initial"),
        ("students", "0030_student_address1_student_address2_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="student_name",
        ),
        migrations.AddField(
            model_name="student",
            name="studenat_name",
            field=models.CharField(
                default="", max_length=255, verbose_name="Student Name"
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="course.coursemodel"
            ),
        ),
    ]