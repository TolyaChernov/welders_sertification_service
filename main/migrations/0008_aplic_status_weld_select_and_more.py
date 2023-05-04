# Generated by Django 4.1.7 on 2023-04-28 07:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0007_alter_application_welder_date_birth"),
    ]

    operations = [
        migrations.CreateModel(
            name="Aplic_status",
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
                (
                    "aplic_num",
                    models.CharField(
                        max_length=100, null=True, verbose_name="Обозначение статуса"
                    ),
                ),
                (
                    "aplic_name",
                    models.CharField(
                        max_length=100,
                        null=True,
                        verbose_name="Название способа сварки",
                    ),
                ),
            ],
            options={
                "verbose_name": "Статус заявки",
                "verbose_name_plural": "Статус заявки",
            },
        ),
        migrations.CreateModel(
            name="Weld_select",
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
                (
                    "select_num",
                    models.CharField(
                        max_length=100, null=True, verbose_name="Обозначение выбора"
                    ),
                ),
                (
                    "select_name",
                    models.CharField(
                        max_length=100, null=True, verbose_name="Название выбора"
                    ),
                ),
            ],
            options={
                "verbose_name": "Статус элемента",
                "verbose_name_plural": "Статус элемента",
            },
        ),
        migrations.AlterField(
            model_name="welding_method",
            name="weld_name",
            field=models.CharField(
                max_length=150, null=True, verbose_name="Полное название способа сварки"
            ),
        ),
        migrations.AlterField(
            model_name="welding_method",
            name="weld_short",
            field=models.CharField(
                max_length=100,
                null=True,
                verbose_name="Краткое название способа сварки",
            ),
        ),
    ]
