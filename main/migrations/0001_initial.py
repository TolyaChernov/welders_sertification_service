# Generated by Django 4.1.7 on 2023-04-21 08:55

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Application",
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
                    "aplic_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата добавления заявки"
                    ),
                ),
                (
                    "aplic_status",
                    models.CharField(
                        choices=[
                            ("1", "Подана"),
                            ("2", "Подтверждена"),
                            ("3", "Отменена"),
                            ("4", "Выполнена"),
                        ],
                        max_length=15,
                        null=True,
                        verbose_name="Статус заявки",
                    ),
                ),
                (
                    "user_fio",
                    models.CharField(
                        max_length=150, null=True, verbose_name="ФИО заявителя"
                    ),
                ),
                (
                    "user_telephon",
                    models.CharField(
                        max_length=150, null=True, verbose_name="Телефон заявителя"
                    ),
                ),
                (
                    "user_email",
                    models.CharField(
                        max_length=150,
                        null=True,
                        verbose_name="Электронная почта заявителя",
                    ),
                ),
                (
                    "org_name",
                    models.CharField(
                        max_length=150,
                        null=True,
                        verbose_name="Наименование организации",
                    ),
                ),
                (
                    "org_adress_ur",
                    models.CharField(
                        max_length=150,
                        null=True,
                        verbose_name="Адрес организации (юридический)",
                    ),
                ),
                (
                    "org_adress_f",
                    models.CharField(
                        max_length=150,
                        null=True,
                        verbose_name="Адрес организации (фактический)",
                    ),
                ),
                (
                    "org_bank_name",
                    models.CharField(
                        max_length=150, null=True, verbose_name="Банк"),
                ),
                (
                    "org_bank_adress",
                    models.CharField(
                        max_length=150, null=True, verbose_name="Адрес банка"
                    ),
                ),
                (
                    "org_bank_rs",
                    models.CharField(
                        max_length=150, null=True, verbose_name="Рассчетный счет"
                    ),
                ),
                (
                    "org_bank_kod",
                    models.CharField(
                        max_length=150, null=True, verbose_name="Код банка"
                    ),
                ),
                (
                    "org_bank_unp",
                    models.CharField(
                        max_length=150, null=True, verbose_name="УНП"),
                ),
                (
                    "org_bank_okpo",
                    models.CharField(
                        max_length=150, null=True, verbose_name="ОКПО"),
                ),
                (
                    "org_contakt_data",
                    models.CharField(
                        max_length=150, null=True, verbose_name="Контактные данные"
                    ),
                ),
                (
                    "org_director_name",
                    models.CharField(
                        max_length=150, null=True, verbose_name="Ф.И.О. руководителя"
                    ),
                ),
                (
                    "org_deystvie",
                    models.CharField(
                        max_length=150, null=True, verbose_name="Действует на основании"
                    ),
                ),
                (
                    "sposob_svarki",
                    models.CharField(
                        max_length=150, null=True, verbose_name="Способ сварки"
                    ),
                ),
                (
                    "sheet_butt_weld",
                    models.CharField(
                        choices=[("0", "Не заявлено"), ("1", "Заявлено")],
                        max_length=15,
                        null=True,
                        verbose_name="Лист - Стыковой шов",
                    ),
                ),
                (
                    "sheet_butt_weld_steel_grade",
                    models.CharField(
                        max_length=150,
                        null=True,
                        verbose_name="Марка стали листа - Стыковой шов",
                    ),
                ),
                (
                    "sheet_butt_weld_min_thickn",
                    models.CharField(
                        max_length=150,
                        null=True,
                        verbose_name="Минимальная толщина листа - Стыковой шов",
                    ),
                ),
                (
                    "sheet_butt_weld_max_thickn",
                    models.CharField(
                        max_length=150,
                        null=True,
                        verbose_name="Максимальная толщина листа - Стыковой шов",
                    ),
                ),
                (
                    "sheet_butt_weld_max_position",
                    models.CharField(
                        max_length=150,
                        null=True,
                        verbose_name="Пространственное положение листа - Стыковой шов",
                    ),
                ),
                (
                    "sheet_fillet_weld",
                    models.CharField(
                        choices=[("0", "Не заявлено"), ("1", "Заявлено")],
                        max_length=15,
                        null=True,
                        verbose_name="Лист - Угловой шов",
                    ),
                ),
                (
                    "sheet_fillet_weld_steel_grade",
                    models.CharField(
                        max_length=150,
                        null=True,
                        verbose_name="Марка стали листа - Угловой шов",
                    ),
                ),
                (
                    "sheet_fillet_weld_min_thickn",
                    models.CharField(
                        max_length=150,
                        null=True,
                        verbose_name="Минимальная толщина листа - Угловой шов",
                    ),
                ),
                (
                    "sheet_fillet_weld_max_thickn",
                    models.CharField(
                        max_length=150,
                        null=True,
                        verbose_name="Максимальная толщина листа - Угловой шов",
                    ),
                ),
                (
                    "sheet_fillet_weld_max_position",
                    models.CharField(
                        max_length=150,
                        null=True,
                        verbose_name="Пространственное положение листа - Угловой шов",
                    ),
                ),
                (
                    "tube_butt_weld",
                    models.CharField(
                        choices=[("0", "Не заявлено"), ("1", "Заявлено")],
                        max_length=15,
                        null=True,
                        verbose_name="Труба - Стыковой шов",
                    ),
                ),
                (
                    "tube_butt_weld_steel_grade",
                    models.CharField(
                        max_length=150,
                        null=True,
                        verbose_name="Марка стали трубы - Стыковой шов",
                    ),
                ),
                (
                    "tube_butt_weld_min_thickn",
                    models.CharField(
                        max_length=150,
                        null=True,
                        verbose_name="Минимальная толщина стенки трубы - Стыковой шов",
                    ),
                ),
                (
                    "tube_butt_weld_max_thickn",
                    models.CharField(
                        max_length=150,
                        null=True,
                        verbose_name="Максимальная толщина стенки трубы - Стыковой шов",
                    ),
                ),
                (
                    "tube_butt_weld_min_diam",
                    models.CharField(
                        max_length=150,
                        null=True,
                        verbose_name="Минимальный диаметр трубы - Стыковой шов",
                    ),
                ),
                (
                    "tube_butt_weld_max_diam",
                    models.CharField(
                        max_length=150,
                        null=True,
                        verbose_name="Максимальный диаметр трубы - Стыковой шов",
                    ),
                ),
                (
                    "tube_butt_weld_max_position",
                    models.CharField(
                        max_length=150,
                        null=True,
                        verbose_name="Пространственное положение  трубы - Стыковой шов",
                    ),
                ),
                (
                    "tube_fillet_weld",
                    models.CharField(
                        choices=[("0", "Не заявлено"), ("1", "Заявлено")],
                        max_length=15,
                        null=True,
                        verbose_name="Труба - Угловой шов",
                    ),
                ),
                (
                    "tube_fillet_weld_steel_grade",
                    models.CharField(
                        max_length=150,
                        null=True,
                        verbose_name="Марка стали трубы - Угловой шов",
                    ),
                ),
                (
                    "tube_fillet_weld_min_thickn",
                    models.CharField(
                        max_length=150,
                        null=True,
                        verbose_name="Минимальная толщина стенки трубы - Угловой шов",
                    ),
                ),
                (
                    "tube_fillet_weld_max_thickn",
                    models.CharField(
                        max_length=150,
                        null=True,
                        verbose_name="Максимальная толщина стенки трубы - Угловой шов",
                    ),
                ),
                (
                    "tube_fillet_weld_min_diam",
                    models.CharField(
                        max_length=150,
                        null=True,
                        verbose_name="Минимальный диаметр трубы - Угловой шов",
                    ),
                ),
                (
                    "tube_fillet_weld_max_diam",
                    models.CharField(
                        max_length=150,
                        null=True,
                        verbose_name="Максимальный диаметр трубы - Угловой шов",
                    ),
                ),
                (
                    "tube_fillet_weld_max_position",
                    models.CharField(
                        max_length=150,
                        null=True,
                        verbose_name="Пространственное положение  трубы - Угловой шов",
                    ),
                ),
                (
                    "gpn",
                    models.CharField(
                        max_length=150,
                        null=True,
                        verbose_name="Подведомственные Госпромнадзору МЧС РБ",
                    ),
                ),
                (
                    "mas",
                    models.CharField(
                        max_length=150,
                        null=True,
                        verbose_name="Подведомственные Министерству архитектуры и строительства РБ",
                    ),
                ),
                (
                    "welder_name",
                    models.CharField(
                        max_length=150, null=True, verbose_name="Имя сварщика"
                    ),
                ),
                (
                    "welder_brand",
                    models.CharField(
                        max_length=150, null=True, verbose_name="Клеймо сварщика"
                    ),
                ),
                (
                    "welder_passport",
                    models.CharField(
                        max_length=150, null=True, verbose_name="Паспорт сварщика"
                    ),
                ),
                (
                    "welder_date_birth",
                    models.CharField(
                        max_length=150, null=True, verbose_name="Дата рождения сварщика"
                    ),
                ),
            ],
            options={
                "verbose_name": "Заявка",
                "verbose_name_plural": "Заявки",
            },
        ),
        migrations.CreateModel(
            name="Welding_method",
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
                    "weld_des",
                    models.CharField(
                        max_length=100,
                        null=True,
                        verbose_name="Обозначение способа сварки",
                    ),
                ),
                (
                    "weld_short",
                    models.CharField(
                        max_length=100,
                        null=True,
                        verbose_name="Краткое обозначение способа сварки",
                    ),
                ),
                (
                    "weld_name",
                    models.CharField(
                        max_length=150,
                        null=True,
                        verbose_name="Полное обозначение способа сварки",
                    ),
                ),
            ],
            options={
                "verbose_name": "Способ сварки",
                "verbose_name_plural": "Способы сварки",
            },
        ),
    ]
