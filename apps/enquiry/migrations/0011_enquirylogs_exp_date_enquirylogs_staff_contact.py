# Generated by Django 5.0 on 2023-12-27 08:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "enquiry",
            "0010_enquirylogs_contact_by_alter_enquiry_studying_course_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="enquirylogs",
            name="exp_date",
            field=models.DateField(
                default=datetime.datetime(
                    2023, 12, 27, 8, 29, 23, 212693, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Expected date",
            ),
        ),
        migrations.AddField(
            model_name="enquirylogs",
            name="staff_contact",
            field=models.CharField(
                default="Shanthi", max_length=255, verbose_name="Contacted Staff"
            ),
        ),
    ]