# Generated by Django 5.0 on 2023-12-28 13:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("enquiry", "0014_remove_enquiry_age"),
    ]

    operations = [
        migrations.AddField(
            model_name="enquiry",
            name="district",
            field=models.CharField(
                blank=True, default=None, max_length=255, verbose_name="District"
            ),
        ),
        migrations.AddField(
            model_name="enquiry",
            name="taluka",
            field=models.CharField(
                blank=True, default=None, max_length=255, verbose_name="Taluk"
            ),
        ),
        migrations.AlterField(
            model_name="enquiry",
            name="f_name",
            field=models.CharField(
                default="", max_length=255, verbose_name="Father Name"
            ),
        ),
        migrations.AlterField(
            model_name="enquiry",
            name="gender",
            field=models.CharField(
                choices=[("male", "Male"), ("female", "Female"), ("others", "others")],
                default="male",
                max_length=10,
                verbose_name="Gender",
            ),
        ),
        migrations.AlterField(
            model_name="enquiry",
            name="known_csc",
            field=models.CharField(
                choices=[
                    ("Television", "Television"),
                    ("Newspaper", "Newspaper"),
                    ("Friend recommend", "Friend recommend"),
                    ("Poster", "Poster"),
                    ("others", "others"),
                ],
                default="Newspaper",
                max_length=1024,
                verbose_name="How You Know about CSC",
            ),
        ),
        migrations.AlterField(
            model_name="enquiry",
            name="name",
            field=models.CharField(default="", max_length=255, verbose_name="Name"),
        ),
        migrations.AlterField(
            model_name="enquiry",
            name="need_of_study",
            field=models.CharField(
                choices=[
                    ("For a job", "For a job"),
                    (
                        "For a job in software profession",
                        "For a job in software profession",
                    ),
                    ("For advance study", "For advance study"),
                    ("Sponsored by company", "Sponsored by company"),
                    ("others", "others"),
                ],
                default="For a job",
                max_length=1024,
                verbose_name="Reason for Study",
            ),
        ),
        migrations.AlterField(
            model_name="enquiry",
            name="qualification_status",
            field=models.CharField(
                choices=[
                    ("Completed", "Completed"),
                    ("Undergoing", "Undergoing"),
                    ("others", "others"),
                ],
                default="Completed",
                max_length=50,
                verbose_name="Qualification Status",
            ),
        ),
        migrations.AlterField(
            model_name="enquiry",
            name="student_college_name",
            field=models.CharField(
                blank=True,
                default="",
                max_length=1055,
                null=True,
                verbose_name="School/College Name",
            ),
        ),
        migrations.AlterField(
            model_name="enquiry",
            name="student_role",
            field=models.CharField(
                choices=[
                    ("Employed", "Employed"),
                    ("Unemployed", "Unemployed"),
                    ("Housewife", "Housewife"),
                    ("Businessman", "Businessman"),
                    ("Student", "Student"),
                    ("Others", "Others"),
                ],
                default="Student",
                max_length=1024,
                verbose_name="Occupation",
            ),
        ),
        migrations.AlterField(
            model_name="enquiry",
            name="studying_year",
            field=models.IntegerField(
                default=None, null=True, verbose_name="Current year"
            ),
        ),
    ]
