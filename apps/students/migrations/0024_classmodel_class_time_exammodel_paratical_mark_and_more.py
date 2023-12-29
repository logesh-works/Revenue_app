# Generated by Django 5.0 on 2023-12-28 14:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("students", "0023_student_district_student_pincode_student_remark_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="classmodel",
            name="class_time",
            field=models.TimeField(blank=True, null=True, verbose_name="Class Time"),
        ),
        migrations.AddField(
            model_name="exammodel",
            name="paratical_mark",
            field=models.FloatField(
                blank=True, default=None, verbose_name="Paratical mark"
            ),
        ),
        migrations.AddField(
            model_name="exammodel",
            name="theory_mark",
            field=models.FloatField(
                blank=True, default=None, null=True, verbose_name="Theory mark"
            ),
        ),
        migrations.AlterField(
            model_name="exammodel",
            name="contected_mode",
            field=models.CharField(
                blank=True,
                choices=[("Online", "Online"), ("Offline", "Offline")],
                default=None,
                max_length=255,
                null=True,
                verbose_name="Contected mode",
            ),
        ),
        migrations.AlterField(
            model_name="exammodel",
            name="mark",
            field=models.FloatField(blank=True, verbose_name="Total mark"),
        ),
        migrations.AlterField(
            model_name="student",
            name="district",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="District",
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="taluka",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="Taluk",
            ),
        ),
    ]