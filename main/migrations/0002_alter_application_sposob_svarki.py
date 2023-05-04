# Generated by Django 4.1.7 on 2023-04-21 09:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="application",
            name="sposob_svarki",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="main.welding_method",
                verbose_name="Способ сварки",
            ),
        ),
    ]
