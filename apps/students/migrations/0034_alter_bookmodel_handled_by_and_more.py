# Generated by Django 5.0 on 2023-12-31 08:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("staffs", "0010_alter_staff_study_year"),
        ("students", "0033_alter_bookmodel_student_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookmodel",
            name="handled_by",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="staffs.staff",
                verbose_name="Handled Staff",
            ),
        ),
        migrations.AlterField(
            model_name="certificatemodel",
            name="issued_by",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="staffs.staff",
                verbose_name="Certificate Issued By",
            ),
        ),
        migrations.AlterField(
            model_name="classmodel",
            name="faculty",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="staffs.staff",
                verbose_name="Handled Staff",
            ),
        ),
    ]