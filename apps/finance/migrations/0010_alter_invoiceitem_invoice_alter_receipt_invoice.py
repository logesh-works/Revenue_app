# Generated by Django 5.0 on 2023-12-30 10:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("finance", "0009_alter_invoice_student"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invoiceitem",
            name="invoice",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="finance.invoice"
            ),
        ),
        migrations.AlterField(
            model_name="receipt",
            name="invoice",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="finance.invoice"
            ),
        ),
    ]
