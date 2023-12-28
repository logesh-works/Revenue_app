# Generated by Django 5.0 on 2023-12-28 17:25

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "students",
            "0026_bookmodel_remark_classmodel_remark_exammodel_remark_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookmodel",
            name="received_date",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="Book received Date"
            ),
        ),
        migrations.AlterField(
            model_name="exammodel",
            name="exam_date",
            field=models.DateField(
                default=django.utils.timezone.now, verbose_name="Examed date"
            ),
        ),
    ]
