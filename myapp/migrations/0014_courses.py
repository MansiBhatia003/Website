# Generated by Django 4.1.7 on 2023-04-07 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0013_universities_enrollment"),
    ]

    operations = [
        migrations.CreateModel(
            name="courses",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("coursename", models.CharField(max_length=1000)),
            ],
        ),
    ]
