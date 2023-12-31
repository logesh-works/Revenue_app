# Generated by Django 5.0 on 2023-12-30 09:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("finance", "0007_receipt_received_by"),
        ("students", "0033_alter_bookmodel_student_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invoice",
            name="student",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.PROTECT,
                to="students.student",
            ),
        ),
        migrations.AlterField(
            model_name="invoiceitem",
            name="invoice",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="finance.invoice"
            ),
        ),
        migrations.AlterField(
            model_name="receipt",
            name="invoice",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="finance.invoice"
            ),
        ),
    ]
