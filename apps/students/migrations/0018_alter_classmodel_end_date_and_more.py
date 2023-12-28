# Generated by Django 5.0 on 2023-12-28 09:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("students", "0017_classmodel_end_date_classmodel_faculty_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="classmodel",
            name="end_date",
            field=models.DateField(verbose_name="Ended on"),
        ),
        migrations.AlterField(
            model_name="classmodel",
            name="start_date",
            field=models.DateField(verbose_name="Started on"),
        ),
        migrations.AlterField(
            model_name="classmodel",
            name="student",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="students.student",
            ),
        ),
    ]
