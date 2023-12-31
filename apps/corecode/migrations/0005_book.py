# Generated by Django 5.0 on 2023-12-30 11:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("corecode", "0004_alter_academicsession_current_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, unique=True)),
            ],
            options={
                "ordering": ["name"],
            },
        ),
    ]