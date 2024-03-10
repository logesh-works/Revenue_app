# Generated by Django 5.0.3 on 2024-03-09 17:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0005_courseexammodel"),
        ("students", "0039_alter_exammodel_subject"),
    ]

    operations = [
        migrations.AlterField(
            model_name="certificatemodel",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="course.coursemodel"
            ),
        ),
    ]