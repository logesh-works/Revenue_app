# Generated by Django 5.0 on 2023-12-31 13:21

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("staffs", "0010_alter_staff_study_year"),
    ]

    operations = [
        migrations.AddField(
            model_name="staff",
            name="address1",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="Address Line 2",
            ),
        ),
        migrations.AddField(
            model_name="staff",
            name="address2",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="Address Line 3",
            ),
        ),
        migrations.AddField(
            model_name="staff",
            name="district",
            field=models.CharField(
                blank=True, default="", max_length=255, verbose_name="District"
            ),
        ),
        migrations.AddField(
            model_name="staff",
            name="pincode",
            field=models.IntegerField(blank=True, default=None, verbose_name="Pincode"),
        ),
        migrations.AddField(
            model_name="staff",
            name="taluka",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="Taluk",
            ),
        ),
        migrations.AlterField(
            model_name="staff",
            name="address",
            field=models.CharField(
                blank=True, default=None, max_length=255, verbose_name="Address"
            ),
        ),
        migrations.AlterField(
            model_name="staff",
            name="date_of_admission",
            field=models.DateField(
                default=django.utils.timezone.now, verbose_name="Date of Join"
            ),
        ),
    ]
