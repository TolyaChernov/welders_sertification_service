# Generated by Django 4.1.7 on 2023-04-28 08:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0009_alter_application_aplic_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="application",
            name="sheet_butt_weld",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="main.weld_select",
                verbose_name="Лист - Стыковой шов",
            ),
        ),
    ]
