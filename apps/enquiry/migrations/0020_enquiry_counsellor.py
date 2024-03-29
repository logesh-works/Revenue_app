# Generated by Django 5.0 on 2023-12-31 08:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("enquiry", "0019_alter_enquirylogs_student"),
        ("staffs", "0008_alter_staff_passport"),
    ]

    operations = [
        migrations.AddField(
            model_name="enquiry",
            name="counsellor",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="staffs.staff",
            ),
        ),
    ]
