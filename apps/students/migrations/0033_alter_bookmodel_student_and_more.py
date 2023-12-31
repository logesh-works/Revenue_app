# Generated by Django 5.0 on 2023-12-30 09:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("course", "0002_alter_coursebookmodel_course_and_more"),
        ("enquiry", "0019_alter_enquirylogs_student"),
        ("students", "0032_rename_studenat_name_student_student_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookmodel",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="students.student"
            ),
        ),
        migrations.AlterField(
            model_name="certificatemodel",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="students.student"
            ),
        ),
        migrations.AlterField(
            model_name="classmodel",
            name="student",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="students.student",
            ),
        ),
        migrations.AlterField(
            model_name="exammodel",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="students.student"
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="course.coursemodel"
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="if_enq",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="enquiry.enquiry",
            ),
        ),
    ]
