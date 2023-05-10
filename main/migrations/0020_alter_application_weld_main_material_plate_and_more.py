# Generated by Django 4.1.7 on 2023-05-10 11:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0019_remove_application_sheet_butt_weld_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="application",
            name="weld_main_material_plate",
            field=models.CharField(
                default="---",
                max_length=2000,
                null=True,
                verbose_name="Материал основной - Лист",
            ),
        ),
        migrations.AlterField(
            model_name="application",
            name="weld_main_material_tube",
            field=models.CharField(
                default="---",
                max_length=2000,
                null=True,
                verbose_name="Материал основной - Труба",
            ),
        ),
        migrations.AlterField(
            model_name="application",
            name="welder_card_id",
            field=models.CharField(
                default="---",
                max_length=2000,
                null=True,
                verbose_name="Номер удостоверения сварщика",
            ),
        ),
        migrations.AlterField(
            model_name="application",
            name="welder_material",
            field=models.CharField(
                default="---",
                max_length=2000,
                null=True,
                verbose_name="Сварочный материал",
            ),
        ),
    ]