# Generated by Django 5.0 on 2023-12-31 08:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("staffs", "0009_alter_staff_quali"),
    ]

    operations = [
        migrations.AlterField(
            model_name="staff",
            name="study_year",
            field=models.IntegerField(
                blank=True, default=None, null=True, verbose_name="If undergoing Year"
            ),
        ),
    ]
