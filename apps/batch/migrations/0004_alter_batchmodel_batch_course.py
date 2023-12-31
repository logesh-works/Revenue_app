# Generated by Django 5.0 on 2023-12-31 11:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("batch", "0003_alter_batchmodel_batch_course_and_more"),
        ("corecode", "0008_exam"),
    ]

    operations = [
        migrations.AlterField(
            model_name="batchmodel",
            name="batch_course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="corecode.subject",
                verbose_name="Batch subject",
            ),
        ),
    ]