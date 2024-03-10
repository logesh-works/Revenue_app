# Generated by Django 5.0.3 on 2024-03-09 17:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("corecode", "0009_time"),
        ("students", "0038_alter_bookmodel_received_book"),
    ]

    operations = [
        migrations.AlterField(
            model_name="exammodel",
            name="subject",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="corecode.subject"
            ),
        ),
    ]
