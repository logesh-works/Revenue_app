# Generated by Django 5.0 on 2023-12-30 06:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CourseModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("Active", "Active"), ("Inactive", "Inactive")],
                        default="Active",
                        max_length=255,
                        verbose_name="Course Status",
                    ),
                ),
                (
                    "course_name",
                    models.CharField(
                        default="", max_length=1024, verbose_name="Course Full Name"
                    ),
                ),
                (
                    "course_s_name",
                    models.CharField(
                        default="", max_length=1024, verbose_name="Course Short Name"
                    ),
                ),
                (
                    "course_duration",
                    models.CharField(
                        default=None, max_length=255, verbose_name="Course Duration"
                    ),
                ),
                ("course_fee", models.IntegerField(verbose_name="Course Fee")),
            ],
        ),
        migrations.CreateModel(
            name="CourseBookModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "book_name",
                    models.CharField(
                        default="", max_length=255, verbose_name="Book Name"
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="course.coursemodel",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CourseSubjectModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sub_name",
                    models.CharField(
                        default="", max_length=255, verbose_name="Subject Name"
                    ),
                ),
                (
                    "sub_duration",
                    models.CharField(
                        default="", max_length=255, verbose_name="Subject Duration"
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="course.coursemodel",
                    ),
                ),
            ],
        ),
    ]