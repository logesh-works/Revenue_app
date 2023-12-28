# Generated by Django 5.0 on 2023-12-28 08:39

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("students", "0016_alter_bookmodel_student"),
    ]

    operations = [
        migrations.AddField(
            model_name="classmodel",
            name="end_date",
            field=models.DateField(
                default=django.utils.timezone.now, verbose_name="Ended on"
            ),
        ),
        migrations.AddField(
            model_name="classmodel",
            name="faculty",
            field=models.CharField(
                default=None, max_length=255, verbose_name="Handled Faculty"
            ),
        ),
        migrations.AddField(
            model_name="classmodel",
            name="finised_subject",
            field=models.CharField(
                default=None, max_length=255, verbose_name="Finised Subject"
            ),
        ),
        migrations.AddField(
            model_name="classmodel",
            name="start_date",
            field=models.DateField(
                default=django.utils.timezone.now, verbose_name="Started on"
            ),
        ),
        migrations.AddField(
            model_name="classmodel",
            name="student",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="students.student",
            ),
        ),
    ]
