from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Material_Plate(models.Model):
    thickness = models.CharField(
        max_length=100, null=True, verbose_name="Толщина листа"
    )

    group_of_material = models.CharField(
        max_length=100, null=True, verbose_name="Группа материала"
    )

    steel_grade = models.CharField(
        max_length=2000, null=True, verbose_name="Марка стали"
    )

    certificate_number = models.CharField(
        max_length=2000, null=True, verbose_name="Сертификат №"
    )

    date = models.CharField(max_length=2000, null=True, verbose_name="Дата")

    class Meta:
        verbose_name = "Материал основной - Лист"
        verbose_name_plural = "Материал основной - Лист"

    def __str__(self):
        return f"{self.thickness, self.group_of_material, self.steel_grade}"


class Material_Tube(models.Model):
    diameter = models.CharField(
        max_length=100,
        null=True,
        verbose_name="Диаметр трубы")

    thickness = models.CharField(
        max_length=100, null=True, verbose_name="Толщина стенки"
    )

    group_of_material = models.CharField(
        max_length=100, null=True, verbose_name="Группа материала"
    )

    steel_grade = models.CharField(
        max_length=2000, null=True, verbose_name="Марка стали"
    )

    certificate_number = models.CharField(
        max_length=2000, null=True, verbose_name="Сертификат №"
    )

    date = models.CharField(max_length=2000, null=True, verbose_name="Дата")

    class Meta:
        verbose_name = "Материал основной - Труба"
        verbose_name_plural = "Материал основной - Труба"

    def __str__(self):
        return (
            f"{self.diameter, self.thickness, self.group_of_material, self.steel_grade}"
        )


class Material_Electrode(models.Model):
    certificate_number = models.CharField(
        max_length=100, null=True, verbose_name="Сертификат №"
    )

    brand = models.CharField(max_length=100, null=True, verbose_name="Марка")

    diameter = models.CharField(
        max_length=100,
        null=True,
        verbose_name="Диаметр")

    date = models.CharField(max_length=2000, null=True, verbose_name="Дата")

    class Meta:
        verbose_name = "Материал вспомогательный - Электрод"
        verbose_name_plural = "Материал вспомогательный - Электрод"

    def __str__(self):
        return f"{self.brand, self.diameter}"


class Material_Rod(models.Model):
    certificate_number = models.CharField(
        max_length=100, null=True, verbose_name="Сертификат №"
    )

    date = models.CharField(max_length=2000, null=True, verbose_name="Дата")

    brand = models.CharField(max_length=100, null=True, verbose_name="Марка")

    diameter = models.CharField(
        max_length=100,
        null=True,
        verbose_name="Диаметр")

    class Meta:
        verbose_name = "Материал вспомогательный - Пруток"
        verbose_name_plural = "Материал вспомогательный - Пруток"

    def __str__(self):
        return f"{self.brand, self.diameter}"


class Material_Wire(models.Model):
    certificate_number = models.CharField(
        max_length=100, null=True, verbose_name="Сертификат №"
    )

    date = models.CharField(max_length=2000, null=True, verbose_name="Дата")

    brand = models.CharField(max_length=100, null=True, verbose_name="Марка")

    diameter = models.CharField(
        max_length=100,
        null=True,
        verbose_name="Диаметр")

    class Meta:
        verbose_name = "Материал вспомогательный - Проволока"
        verbose_name_plural = "Материал вспомогательный - Проволока"

    def __str__(self):
        return f"{self.brand, self.diameter}"


class Material_Flux(models.Model):
    certificate_number = models.CharField(
        max_length=100, null=True, verbose_name="Сертификат №"
    )

    date = models.CharField(max_length=2000, null=True, verbose_name="Дата")

    brand = models.CharField(max_length=100, null=True, verbose_name="Марка")

    class Meta:
        verbose_name = "Материал вспомогательный - Флюс"
        verbose_name_plural = "Материал вспомогательный - Флюс"

    def __str__(self):
        return f"{self.brand}"


class Welding_method(models.Model):
    weld_des = models.CharField(
        max_length=100, null=True, verbose_name="Обозначение способа сварки"
    )

    weld_short = models.CharField(
        max_length=100, null=True, verbose_name="Краткое название способа сварки"
    )

    weld_name = models.CharField(
        max_length=2000, null=True, verbose_name="Полное название способа сварки"
    )

    class Meta:
        verbose_name = "Способ сварки"
        verbose_name_plural = "Способы сварки"

    def __str__(self):
        return f"{self.weld_short}"


class Aplic_status(models.Model):
    aplic_num = models.CharField(
        max_length=100, null=True, verbose_name="Обозначение статуса заявки"
    )

    aplic_name = models.CharField(
        max_length=100, null=True, verbose_name="Название способа сварки"
    )

    class Meta:
        verbose_name = "Статус заявки"
        verbose_name_plural = "Статус заявки"

    def __str__(self):
        return f"{self.aplic_name}"


class Weld_select(models.Model):
    select_num = models.CharField(
        max_length=100, null=True, verbose_name="Обозначение выбора"
    )

    select_name = models.CharField(
        max_length=100, null=True, verbose_name="Название выбора"
    )

    class Meta:
        verbose_name = "Статус элемента"
        verbose_name_plural = "Статус элемента"

    def __str__(self):
        return f"{self.select_name}"


# status = [
#     ("1", "Подана"),
#     ("2", "Подтверждена"),
#     ("3", "Отменена"),
#     ("4", "Выполнена"),
#     # ("5", "+5"),
# ]


select = [
    ("0", "Не заявлено"),
    ("1", "Заявлено"),
]


class Application(models.Model):
    # Данные заявки
    aplic_user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="Пользователь",
    )

    aplic_status = models.ForeignKey(
        Aplic_status,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="Статус заявки",
    )

    aplic_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата добавления заявки"
    )

    # Данные заявителя
    user_fio = models.CharField(
        max_length=2000, null=True, verbose_name="ФИО заявителя"
    )

    user_telephon = models.CharField(
        max_length=2000, null=True, verbose_name="Телефон заявителя"
    )

    user_email = models.CharField(
        max_length=2000, null=True, verbose_name="Электронная почта заявителя"
    )

    # Данные организации
    org_name = models.CharField(
        max_length=2000, null=True, verbose_name="Наименование организации"
    )

    org_adress_ur = models.CharField(
        max_length=2000, null=True, verbose_name="Адрес организации (юридический)"
    )

    org_adress_f = models.CharField(
        max_length=2000, null=True, verbose_name="Адрес организации (фактический)"
    )

    org_bank_name = models.CharField(
        max_length=2000, null=True, verbose_name="Банк")

    org_bank_adress = models.CharField(
        max_length=2000, null=True, verbose_name="Адрес банка"
    )

    org_bank_rs = models.CharField(
        max_length=2000, null=True, verbose_name="Рассчетный счет"
    )

    org_bank_kod = models.CharField(
        max_length=2000, null=True, verbose_name="Код банка"
    )

    org_bank_unp = models.CharField(
        max_length=2000, null=True, verbose_name="УНП")

    org_bank_okpo = models.CharField(
        max_length=2000, null=True, verbose_name="ОКПО")

    org_contakt_data = models.CharField(
        max_length=2000, null=True, verbose_name="Контактные данные"
    )

    org_director_name = models.CharField(
        max_length=2000, null=True, verbose_name="Ф.И.О. руководителя"
    )

    org_deystvie = models.CharField(
        max_length=2000, null=True, verbose_name="Действует на основании"
    )

    sposob_svarki = models.ForeignKey(
        Welding_method,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="Способ сварки",
    )

    # Область распространения - Лист - Стыковые швы
    sheet_butt_weld = models.CharField(
        max_length=15, null=True, choices=select, verbose_name="Лист - Стыковой шов"
    )

    sheet_butt_weld_steel_grade = models.CharField(
        max_length=2000, null=True, verbose_name="Марка стали листа - Стыковой шов"
    )

    sheet_butt_weld_min_thickn = models.CharField(
        max_length=2000,
        null=True,
        verbose_name="Минимальная толщина листа - Стыковой шов",
    )

    sheet_butt_weld_max_thickn = models.CharField(
        max_length=2000,
        null=True,
        verbose_name="Максимальная толщина листа - Стыковой шов",
    )

    sheet_butt_weld_position = models.CharField(
        max_length=2000,
        null=True,
        verbose_name="Пространственное положение листа - Стыковой шов",
    )

    # Область распространения - Лист - Угловой - швы
    sheet_fillet_weld = models.CharField(
        max_length=15, null=True, choices=select, verbose_name="Лист - Угловой шов"
    )

    sheet_fillet_weld_steel_grade = models.CharField(
        max_length=2000, null=True, verbose_name="Марка стали листа - Угловой шов"
    )

    sheet_fillet_weld_min_thickn = models.CharField(
        max_length=2000,
        null=True,
        verbose_name="Минимальная толщина листа - Угловой шов",
    )

    sheet_fillet_weld_max_thickn = models.CharField(
        max_length=2000,
        null=True,
        verbose_name="Максимальная толщина листа - Угловой шов",
    )

    sheet_fillet_weld_position = models.CharField(
        max_length=2000,
        null=True,
        verbose_name="Пространственное положение листа - Угловой шов",
    )

    # Область распространения - Труба - Стыковой шов
    tube_butt_weld = models.CharField(
        max_length=15, null=True, choices=select, verbose_name="Труба - Стыковой шов"
    )

    tube_butt_weld_steel_grade = models.CharField(
        max_length=2000, null=True, verbose_name="Марка стали трубы - Стыковой шов"
    )

    tube_butt_weld_min_thickn = models.CharField(
        max_length=2000,
        null=True,
        verbose_name="Минимальная толщина стенки трубы - Стыковой шов",
    )

    tube_butt_weld_max_thickn = models.CharField(
        max_length=2000,
        null=True,
        verbose_name="Максимальная толщина стенки трубы - Стыковой шов",
    )

    tube_butt_weld_min_diam = models.CharField(
        max_length=2000,
        null=True,
        verbose_name="Минимальный диаметр трубы - Стыковой шов",
    )

    tube_butt_weld_max_diam = models.CharField(
        max_length=2000,
        null=True,
        verbose_name="Максимальный диаметр трубы - Стыковой шов",
    )

    tube_butt_weld_position = models.CharField(
        max_length=2000,
        null=True,
        verbose_name="Пространственное положение  трубы - Стыковой шов",
    )

    # Область распространения - Труба - Угловой шов
    tube_fillet_weld = models.CharField(
        max_length=15, null=True, choices=select, verbose_name="Труба - Угловой шов"
    )

    tube_fillet_weld_steel_grade = models.CharField(
        max_length=2000, null=True, verbose_name="Марка стали трубы - Угловой шов"
    )

    tube_fillet_weld_min_thickn = models.CharField(
        max_length=2000,
        null=True,
        verbose_name="Минимальная толщина стенки трубы - Угловой шов",
    )

    tube_fillet_weld_max_thickn = models.CharField(
        max_length=2000,
        null=True,
        verbose_name="Максимальная толщина стенки трубы - Угловой шов",
    )

    tube_fillet_weld_min_diam = models.CharField(
        max_length=2000,
        null=True,
        verbose_name="Минимальный диаметр трубы - Угловой шов",
    )

    tube_fillet_weld_max_diam = models.CharField(
        max_length=2000,
        null=True,
        verbose_name="Максимальный диаметр трубы - Угловой шов",
    )

    tube_fillet_weld_position = models.CharField(
        max_length=2000,
        null=True,
        verbose_name="Пространственное положение  трубы - Угловой шов",
    )

    # Подведомственность
    gpn = models.CharField(
        max_length=2000,
        null=True,
        verbose_name="Подведомственные Госпромнадзору МЧС РБ",
    )

    mas = models.CharField(
        max_length=2000,
        null=True,
        verbose_name="Подведомственные Министерству архитектуры и строительства РБ",
    )

    # Информация о сварщиках
    welder_name = models.CharField(
        max_length=2000,
        null=True,
        verbose_name="Имя сварщика",
    )

    welder_brand = models.CharField(
        max_length=2000,
        null=True,
        verbose_name="Клеймо сварщика",
    )

    welder_card_id = models.CharField(
        max_length=2000,
        null=True,
        verbose_name="Номер удостоверения сварщика",
    )

    welder_passport = models.CharField(
        max_length=2000,
        null=True,
        verbose_name="Паспорт сварщика",
    )

    welder_date_birth = models.CharField(
        max_length=2000,
        null=True,
        verbose_name="Дата рождения сварщика",
    )

    ###########################
    start_date = models.CharField(
        max_length=2000,
        null=True,
        verbose_name="Дата начала контроля",
    )

    end_date = models.CharField(
        max_length=2000,
        null=True,
        verbose_name="Дата окончания контроля",
    )

    welder_material = models.CharField(
        max_length=2000,
        null=True,
        verbose_name="Сварочный материал",
    )

    weld_main_material_plate = models.CharField(
        max_length=2000,
        null=True,
        verbose_name="Материал основной - Лист",
    )

    weld_main_material_tube = models.CharField(
        max_length=2000,
        null=True,
        verbose_name="Материал основной - Труба",
    )

    # Комиссия
    chef_kom_pos = models.CharField(
        max_length=2000,
        null=True,
        verbose_name="Должность председателя комиссии",
    )

    chef_kom_fio = models.CharField(
        max_length=2000,
        null=True,
        verbose_name="Имя председателя комиссии",
    )

    kom_pos = models.CharField(
        max_length=2000,
        null=True,
        verbose_name="Должность члена комиссии",
    )

    kom_fio = models.CharField(
        max_length=2000,
        null=True,
        verbose_name="Имя члена комиссии",
    )

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return f"{self.aplic_date}"
