# Generated by Django 4.1.7 on 2023-03-28 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0005_myreview"),
    ]

    operations = [
        migrations.AlterField(
            model_name="myreview",
            name="message",
            field=models.TextField(max_length=1000),
        ),
    ]
