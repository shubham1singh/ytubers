# Generated by Django 4.2.1 on 2023-05-11 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("youtubers", "0002_auto_20201130_1517"),
    ]

    operations = [
        migrations.AlterField(
            model_name="youtuber",
            name="height",
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]
