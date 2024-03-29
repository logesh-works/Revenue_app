# Generated by Django 5.0 on 2023-12-28 17:16

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("students", "0025_alter_classmodel_class_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="bookmodel",
            name="remark",
            field=models.CharField(
                blank=True, default=None, max_length=2046, verbose_name="Remark"
            ),
        ),
        migrations.AddField(
            model_name="classmodel",
            name="remark",
            field=models.CharField(
                blank=True, default=None, max_length=2046, verbose_name="Remark"
            ),
        ),
        migrations.AddField(
            model_name="exammodel",
            name="remark",
            field=models.CharField(
                blank=True, default=None, max_length=2046, verbose_name="Remark"
            ),
        ),
        migrations.AlterField(
            model_name="exammodel",
            name="exam_date",
            field=models.DateField(auto_now_add=True, verbose_name="Examed date"),
        ),
        migrations.CreateModel(
            name="Certificatemodel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "course",
                    models.CharField(
                        blank=True, default=None, max_length=255, verbose_name="Course"
                    ),
                ),
                (
                    "date_of_complete",
                    models.DateField(
                        default=django.utils.timezone.now,
                        verbose_name="Date of Completion",
                    ),
                ),
                (
                    "certificate_no",
                    models.IntegerField(
                        blank=True, default=None, verbose_name="Certificate Number"
                    ),
                ),
                (
                    "certificate_date",
                    models.DateField(
                        default=django.utils.timezone.now,
                        verbose_name="Certificate Date",
                    ),
                ),
                (
                    "certificate_issued_date",
                    models.DateField(
                        default=django.utils.timezone.now,
                        verbose_name="Certificate Issued Date",
                    ),
                ),
                (
                    "grade",
                    models.CharField(
                        blank=True,
                        default=None,
                        max_length=10,
                        verbose_name="Grade on Certificate",
                    ),
                ),
                (
                    "issued_by",
                    models.CharField(
                        blank=True,
                        default=None,
                        max_length=10,
                        verbose_name="Certificate Issued By",
                    ),
                ),
                (
                    "remark",
                    models.CharField(
                        blank=True, default=None, max_length=2046, verbose_name="Remark"
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="students.student",
                    ),
                ),
            ],
        ),
    ]
