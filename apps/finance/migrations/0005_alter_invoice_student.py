# Generated by Django 5.0 on 2023-12-28 09:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("finance", "0004_alter_invoice_student"),
        ("students", "0018_alter_classmodel_end_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invoice",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="students.student"
            ),
        ),
    ]
