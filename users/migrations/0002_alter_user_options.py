# Generated by Django 4.1.5 on 2023-02-07 14:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={"verbose_name": "Юзер", "verbose_name_plural": "Юзеры"},
        ),
    ]
