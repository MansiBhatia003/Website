# Generated by Django 4.1.7 on 2023-03-28 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0004_rename_day_article_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="myreview",
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
                ("Title", models.CharField(max_length=100)),
                ("message", models.CharField(max_length=1000)),
            ],
        ),
    ]
