# Generated by Django 5.0 on 2023-12-30 09:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("enquiry", "0018_enquiry_address1_enquiry_address2_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="enquirylogs",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="enquiry.enquiry"
            ),
        ),
    ]