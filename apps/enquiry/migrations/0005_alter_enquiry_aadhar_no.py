# Generated by Django 5.0 on 2023-12-27 04:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("enquiry", "0004_enquiry_aadhar_no"),
    ]

    operations = [
        migrations.AlterField(
            model_name="enquiry",
            name="aadhar_no",
            field=models.BigIntegerField(
                default=None, null=True, verbose_name="Aadhar Number"
            ),
        ),
    ]
