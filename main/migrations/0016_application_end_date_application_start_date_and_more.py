# Generated by Django 4.1.7 on 2023-05-03 17:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0015_alter_aplic_status_aplic_num"),
    ]

    operations = [
        migrations.AddField(
            model_name="application",
            name="end_date",
            field=models.CharField(
                max_length=2000, null=True, verbose_name="Дата окончания контроля"
            ),
        ),
        migrations.AddField(
            model_name="application",
            name="start_date",
            field=models.CharField(
                max_length=2000, null=True, verbose_name="Дата начала контроля"
            ),
        ),
        migrations.AddField(
            model_name="application",
            name="weld_main_material_plate",
            field=models.CharField(
                max_length=2000, null=True, verbose_name="Материал основной - Лист"
            ),
        ),
        migrations.AddField(
            model_name="application",
            name="weld_main_material_tube",
            field=models.CharField(
                max_length=2000, null=True, verbose_name="Материал основной - Труба"
            ),
        ),
        migrations.AddField(
            model_name="application",
            name="welder_material",
            field=models.CharField(
                max_length=2000, null=True, verbose_name="Сварочный материал"
            ),
        ),
    ]
