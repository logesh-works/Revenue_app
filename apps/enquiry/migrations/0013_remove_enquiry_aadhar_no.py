# Generated by Django 5.0 on 2023-12-27 15:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("enquiry", "0012_alter_enquirylogs_exp_date"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="enquiry",
            name="aadhar_no",
        ),
    ]