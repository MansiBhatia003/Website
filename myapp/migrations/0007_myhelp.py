# Generated by Django 4.1.7 on 2023-03-29 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0006_alter_myreview_message"),
    ]

    operations = [
        migrations.CreateModel(
            name="myhelp",
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
                ("message", models.TextField(max_length=1000)),
            ],
        ),
    ]
