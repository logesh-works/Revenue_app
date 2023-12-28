# Generated by Django 5.0 on 2023-12-28 09:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("finance", "0002_receipt_bill_no"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="invoice",
            options={"ordering": ["student"]},
        ),
        migrations.RemoveField(
            model_name="invoice",
            name="balance_from_previous_term",
        ),
        migrations.RemoveField(
            model_name="invoice",
            name="class_for",
        ),
        migrations.RemoveField(
            model_name="invoice",
            name="session",
        ),
        migrations.RemoveField(
            model_name="invoice",
            name="term",
        ),
    ]
