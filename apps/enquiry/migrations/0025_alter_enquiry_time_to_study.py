# Generated by Django 5.0.3 on 2024-03-10 08:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("corecode", "0009_time"),
        ("enquiry", "0024_enquiry_new_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="enquiry",
            name="time_to_study",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="corecode.time",
            ),
        ),
    ]