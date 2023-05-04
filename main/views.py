from .utils import render_to_pdf
from django.http import HttpResponse
from django.db.models import Q
import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User  # , Group
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy

from .forms import *
from .models import *  # Application, Welding_method, Aplic_status


def index(request):
    """
    Description of index

    Args:
        request (undefined):

    """
    title = "Главная"
    # Определение группы пользователя
    username = str(request.user)
    if username != "AnonymousUser":
        user = get_object_or_404(User, username=username)
        group = user.groups.get(user=user.id)
    else:
        group = "No_Group"

    return render(
        request,
        "main/index.html",
        {
            "title": title,
            "group": group,
        },
    )


@login_required(login_url=reverse_lazy("login"))
def add_application(request):
    """
    Description of add_application

    Args:
        request (undefined):

    """
    title = "Заявка"

    # Определение группы пользователя
    username = str(request.user)
    if username == "admin":
        group = "admin"
    else:
        user = get_object_or_404(User, username=username)
        group = str(user.groups.get(user=user.id))

    if request.method == "POST":
        list_name_param = [
            "user_fio",
            "user_telephon",
            "user_email",
            "org_name",
            "org_adress_ur",
            "org_adress_f",
            "org_bank_name",
            "org_bank_adress",
            "org_bank_rs",
            "org_bank_kod",
            "org_bank_unp",
            "org_bank_okpo",
            "org_contakt_data",
            "org_director_name",
            "org_deystvie",
            "sposob_svarki",
            "sheet_butt_weld",
            "sheet_butt_weld_steel_grade",
            "sheet_butt_weld_min_thickn",
            "sheet_butt_weld_max_thickn",
            "sheet_butt_weld_position",
            "sheet_fillet_weld",
            "sheet_fillet_weld_steel_grade",
            "sheet_fillet_weld_min_thickn",
            "sheet_fillet_weld_max_thickn",
            "sheet_fillet_weld_position",
            "tube_butt_weld",
            "tube_butt_weld_steel_grade",
            "tube_butt_weld_min_thickn",
            "tube_butt_weld_max_thickn",
            "tube_butt_weld_min_diam",
            "tube_butt_weld_max_diam",
            "tube_butt_weld_position",
            "tube_fillet_weld",
            "tube_fillet_weld_steel_grade",
            "tube_fillet_weld_min_thickn",
            "tube_fillet_weld_max_thickn",
            "tube_fillet_weld_min_diam",
            "tube_fillet_weld_max_diam",
            "tube_fillet_weld_position",
            "gpn",
            "mas",
            "welder_name",
            "welder_brand",
            "welder_passport",
            "welder_date_birth",
        ]
        list_param = []
        result = dict(request.POST)
        application = Application()
        for i in range(len(list_name_param)):
            name_param = list_name_param[i]
            try:
                param = str(result[name_param])
                param = param[2:-2]
            except KeyError:
                param = "---"
            if param == "":
                param = "---"
            param = param.replace("',", "|")
            param = param.replace("'", "")
            list_param.append(param)

        application.aplic_user = User.objects.get(username=username)
        application.aplic_status = Aplic_status.objects.get(aplic_num=1)
        application.user_fio = list_param[0]
        application.user_telephon = list_param[1]
        application.user_email = list_param[2]
        application.org_name = list_param[3]
        application.org_adress_ur = list_param[4]
        application.org_adress_f = list_param[5]
        application.org_bank_name = list_param[6]
        application.org_bank_adress = list_param[7]
        application.org_bank_rs = list_param[8]
        application.org_bank_kod = list_param[9]
        application.org_bank_unp = list_param[10]
        application.org_bank_okpo = list_param[11]
        application.org_contakt_data = list_param[12]
        application.org_director_name = list_param[13]
        application.org_deystvie = list_param[14]
        try:
            int(list_param[15])
        except ValueError:
            list_param[15] = 0
        try:
            application.sposob_svarki = Welding_method.objects.get(
                weld_des=int(list_param[15])
            )
        except Welding_method.DoesNotExist:
            application.sposob_svarki = None
        application.sheet_butt_weld = list_param[16]
        application.sheet_butt_weld_steel_grade = list_param[17]
        application.sheet_butt_weld_min_thickn = list_param[18]
        application.sheet_butt_weld_max_thickn = list_param[19]
        application.sheet_butt_weld_position = list_param[20]
        application.sheet_fillet_weld = list_param[21]
        application.sheet_fillet_weld_steel_grade = list_param[22]
        application.sheet_fillet_weld_min_thickn = list_param[23]
        application.sheet_fillet_weld_max_thickn = list_param[24]
        application.sheet_fillet_weld_position = list_param[25]
        application.tube_butt_weld = list_param[26]
        application.tube_butt_weld_steel_grade = list_param[27]
        application.tube_butt_weld_min_thickn = list_param[28]
        application.tube_butt_weld_max_thickn = list_param[29]
        application.tube_butt_weld_min_diam = list_param[30]
        application.tube_butt_weld_max_diam = list_param[31]
        application.tube_butt_weld_position = list_param[32]
        application.tube_fillet_weld = list_param[33]
        application.tube_fillet_weld_steel_grade = list_param[34]
        application.tube_fillet_weld_min_thickn = list_param[35]
        application.tube_fillet_weld_max_thickn = list_param[36]
        application.tube_fillet_weld_min_diam = list_param[37]
        application.tube_fillet_weld_max_diam = list_param[38]
        application.tube_fillet_weld_position = list_param[39]
        application.gpn = list_param[40]
        application.mas = list_param[41]
        application.welder_name = list_param[42]
        application.welder_brand = list_param[43]
        application.welder_passport = list_param[44]
        application.welder_date_birth = list_param[45]
        application.save()

    return render(
        request,
        "main/application.html",
        {
            "title": title,
            "group": group,
        },
    )


@login_required(login_url=reverse_lazy("login"))
def private_office(request):
    """
    Description of private_office

    Args:
        request (undefined):

    """
    title = "Личный кабинет"

    username = str(request.user)
    if username == "admin":
        group = "admin"
    else:
        user = get_object_or_404(User, username=username)
        group = str(user.groups.get(user=user.id))

    if group == "customer" or group == "admin":
        return render(
            request,
            "main/private_office_s1.html",
            {
                "title": title,
                "group": group,
            },
        )
    elif group == "engineer" or group == "admin":
        return render(
            request,
            "main/private_office_s1.html",
            {
                "title": title,
                "group": group,
            },
        )


def test_card(request):
    """
    Description of test_card

    Args:
        request (undefined):

    """
    title = "Проверка удостоверения"

    form = SearchForm()
    from django.db.models import Q

    message = ""
    title = "Результаты поиска"
    result = []
    if request.method == "GET":
        query_name = request.GET.get("welder_name", "")
        query_brand = request.GET.get("welder_brand", "")
        query_id_card = request.GET.get("welder_card_id", "")

        if query_name == query_brand == query_id_card == "":
            message = "ВНИМАНИЕ: Заполните одно из полей"
            return render(
                request,
                "main/test_card.html",
                {
                    "title": title,
                    "form": form,
                },
            )
        else:
            result = Application.objects.filter(
                Q(welder_name__icontains=query_name)
                & Q(welder_brand__icontains=query_brand)
                | Q(welder_card_id__icontains=query_id_card)
            )


            return render(
                request,
                "main/test_card.html",
                {
                    "title": title,
                    "result": result,
                    "form": form,
                    "query_name": query_name,
                    "query_brand": query_brand,
                    "query_id_card": query_id_card,
                    "message": message,
                },
            )

    return render(
        request,
        "main/test_card.html",
        {
            "title": title,
            "form": form,
        },
    )


@login_required(login_url=reverse_lazy("login"))
def all_applications(request):
    """
    Description of all_applications

    Args:
        request (undefined):

    """
    title = "Заявка"

    # Определение группы пользователя
    username = str(request.user)
    username = str(request.user)
    if username == "admin":
        group = "admin"
    else:
        user = get_object_or_404(User, username=username)
        group = str(user.groups.get(user=user.id))

    result = Application.objects.filter(aplic_user_id=request.user.id).order_by(
        "-aplic_date"
    )

    return render(
        request,
        "main/all_applications.html",
        {
            "title": title,
            "result": result,
            "group": group,
        },
    )



@login_required(login_url=reverse_lazy("login"))
def all_applications_give(request):
    """
    Description of all_applications_give

    Args:
        request (undefined):

    """
    title = "Заявки поданные"

    # Определение группы пользователя
    username = str(request.user)
    username = str(request.user)
    if username == "admin":
        group = "admin"
    else:
        user = get_object_or_404(User, username=username)
        group = str(user.groups.get(user=user.id))

    if group == "customer":
        result = Application.objects.filter(
            Q(aplic_status_id="1") & Q(aplic_user_id=request.user.id)
        ).order_by("-aplic_date")
    elif group == "engineer":
        result = Application.objects.filter(
            aplic_status_id="1").order_by("-aplic_date")

    return render(
        request,
        "main/all_applications_give.html",
        {
            "title": title,
            "result": result,
            "group": group,
        },
    )


@login_required(login_url=reverse_lazy("login"))
def all_applications_confirm(request):
    """
    Description of all_applications_confirm

    Args:
        request (undefined):

    """
    title = "Заявки подтвержденные"

    # Определение группы пользователя
    username = str(request.user)
    username = str(request.user)
    if username == "admin":
        group = "admin"
    else:
        user = get_object_or_404(User, username=username)
        group = str(user.groups.get(user=user.id))

    if group == "customer":
        result = Application.objects.filter(
            Q(aplic_status_id="2") & Q(aplic_user_id=request.user.id)
        ).order_by("-aplic_date")
    elif group == "engineer":
        result = Application.objects.filter(
            aplic_status_id="2").order_by("-aplic_date")

    return render(
        request,
        "main/all_applications_confirm.html",
        {
            "title": title,
            "result": result,
            "group": group,
        },
    )


@login_required(login_url=reverse_lazy("login"))
def all_applications_cancel(request):
    """
    Description of all_applications_cancel

    Args:
        request (undefined):

    """
    title = "Заявки отмененные"
    # Определение группы пользователя
    username = str(request.user)
    username = str(request.user)
    if username == "admin":
        group = "admin"
    else:
        user = get_object_or_404(User, username=username)
        group = str(user.groups.get(user=user.id))

    if group == "customer":
        result = Application.objects.filter(
            Q(aplic_status_id="3") & Q(aplic_user_id=request.user.id)
        ).order_by("-aplic_date")
    elif group == "engineer":
        result = Application.objects.filter(
            aplic_status_id="3").order_by("-aplic_date")
    return render(
        request,
        "main/all_applications_cancel.html",
        {
            "title": title,
            "result": result,
            "group": group,
        },
    )


@login_required(login_url=reverse_lazy("login"))
def all_applications_done(request):
    """
    Description of all_applications_done

    Args:
        request (undefined):

    """
    title = "Заявки выполненные"
    # Определение группы пользователя
    username = str(request.user)
    username = str(request.user)
    if username == "admin":
        group = "admin"
    else:
        user = get_object_or_404(User, username=username)
        group = str(user.groups.get(user=user.id))

    if group == "customer":
        result = Application.objects.filter(
            Q(aplic_status_id="4") & Q(aplic_user_id=request.user.id)
        ).order_by("-aplic_date")
    elif group == "engineer":
        result = Application.objects.filter(
            aplic_status_id="4").order_by("-aplic_date")
    return render(
        request,
        "main/all_applications_done.html",
        {
            "title": title,
            "result": result,
            "group": group,
        },
    )


@login_required(login_url=reverse_lazy("login"))
def application_update(request, pk: int):
    """
    Description of application_update

    Args:
        request (undefined):
        pk (int):

    """
    title = "Редактирование заявки"
    username = str(request.user)
    if username == "admin":
        group = "admin"
    else:
        user = get_object_or_404(User, username=username)
        group = str(user.groups.get(user=user.id))
    result = Application.objects.filter(pk=pk).first()
    # Список сварщиков для application_update.html
    list = []
    welder_name = result.welder_name
    welder_name = welder_name.split("| ")
    welder_brand = result.welder_brand
    welder_brand = welder_brand.split("| ")
    welder_passport = result.welder_passport
    welder_passport = welder_passport.split("| ")
    welder_date_birth = result.welder_date_birth
    welder_date_birth = welder_date_birth.split("| ")
    list = []
    for i in range(len(welder_name)):
        default = []
        default.append(welder_name[i])
        default.append(welder_brand[i])
        default.append(welder_passport[i])
        default.append(welder_date_birth[i])
        list.append(default)
    list_name_param = [
        "user_fio",
        "user_telephon",
        "user_email",
        "org_name",
        "org_adress_ur",
        "org_adress_f",
        "org_bank_name",
        "org_bank_adress",
        "org_bank_rs",
        "org_bank_kod",
        "org_bank_unp",
        "org_bank_okpo",
        "org_contakt_data",
        "org_director_name",
        "org_deystvie",
        "sposob_svarki",
        "sheet_butt_weld",
        "sheet_butt_weld_steel_grade",
        "sheet_butt_weld_min_thickn",
        "sheet_butt_weld_max_thickn",
        "sheet_butt_weld_position",
        "sheet_fillet_weld",
        "sheet_fillet_weld_steel_grade",
        "sheet_fillet_weld_min_thickn",
        "sheet_fillet_weld_max_thickn",
        "sheet_fillet_weld_position",
        "tube_butt_weld",
        "tube_butt_weld_steel_grade",
        "tube_butt_weld_min_thickn",
        "tube_butt_weld_max_thickn",
        "tube_butt_weld_min_diam",
        "tube_butt_weld_max_diam",
        "tube_butt_weld_position",
        "tube_fillet_weld",
        "tube_fillet_weld_steel_grade",
        "tube_fillet_weld_min_thickn",
        "tube_fillet_weld_max_thickn",
        "tube_fillet_weld_min_diam",
        "tube_fillet_weld_max_diam",
        "tube_fillet_weld_position",
        "gpn",
        "mas",
        "welder_name",
        "welder_brand",
        "welder_passport",
        "welder_date_birth",
    ]
    if request.method == "POST":
        list_param = []
        result = dict(request.POST)
        application = Application.objects.filter(pk=pk).first()
        for i in range(len(list_name_param)):
            name_param = list_name_param[i]
            try:
                param = str(result[name_param])
                param = param[2:-2]
            except KeyError:
                param = "---"
            if param == "":
                param = "---"
            param = param.replace("',", "|")
            param = param.replace("'", "")
            list_param.append(param)

        application.aplic_status = Aplic_status.objects.get(aplic_num=1)
        application.user_fio = list_param[0]
        application.user_telephon = list_param[1]
        application.user_email = list_param[2]
        application.org_name = list_param[3]
        application.org_adress_ur = list_param[4]
        application.org_adress_f = list_param[5]
        application.org_bank_name = list_param[6]
        application.org_bank_adress = list_param[7]
        application.org_bank_rs = list_param[8]
        application.org_bank_kod = list_param[9]
        application.org_bank_unp = list_param[10]
        application.org_bank_okpo = list_param[11]
        application.org_contakt_data = list_param[12]
        application.org_director_name = list_param[13]
        application.org_deystvie = list_param[14]
        try:
            int(list_param[15])
        except ValueError:
            list_param[15] = 0
        try:
            application.sposob_svarki = Welding_method.objects.get(
                weld_des=int(list_param[15])
            )
        except Welding_method.DoesNotExist:
            application.sposob_svarki = None
        application.sheet_butt_weld = list_param[16]
        application.sheet_butt_weld_steel_grade = list_param[17]
        application.sheet_butt_weld_min_thickn = list_param[18]
        application.sheet_butt_weld_max_thickn = list_param[19]
        application.sheet_butt_weld_position = list_param[20]
        application.sheet_fillet_weld = list_param[21]
        application.sheet_fillet_weld_steel_grade = list_param[22]
        application.sheet_fillet_weld_min_thickn = list_param[23]
        application.sheet_fillet_weld_max_thickn = list_param[24]
        application.sheet_fillet_weld_position = list_param[25]
        application.tube_butt_weld = list_param[26]
        application.tube_butt_weld_steel_grade = list_param[27]
        application.tube_butt_weld_min_thickn = list_param[28]
        application.tube_butt_weld_max_thickn = list_param[29]
        application.tube_butt_weld_min_diam = list_param[30]
        application.tube_butt_weld_max_diam = list_param[31]
        application.tube_butt_weld_position = list_param[32]
        application.tube_fillet_weld = list_param[33]
        application.tube_fillet_weld_steel_grade = list_param[34]
        application.tube_fillet_weld_min_thickn = list_param[35]
        application.tube_fillet_weld_max_thickn = list_param[36]
        application.tube_fillet_weld_min_diam = list_param[37]
        application.tube_fillet_weld_max_diam = list_param[38]
        application.tube_fillet_weld_position = list_param[39]
        application.gpn = list_param[40]
        application.mas = list_param[41]
        application.welder_name = list_param[42]
        application.welder_brand = list_param[43]
        application.welder_passport = list_param[44]
        application.welder_date_birth = list_param[45]
        application.save()
        return redirect("all_applications_give")
    
    return render(
        request,
        "main/application_update.html",
        {
            "title": title,
            "result": result,
            "list": list,
            "group": group,
        },
    )


@login_required(login_url=reverse_lazy("login"))
def application_complete_akt(request, pk: int):
    """
    Description of application_complete_akt

    Args:
        request (undefined):
        pk (int):

    """
    title = "Редактирование заявки"
    username = str(request.user)
    if username == "admin":
        group = "admin"
    else:
        user = get_object_or_404(User, username=username)
        group = str(user.groups.get(user=user.id))
    result = Application.objects.filter(pk=pk).first()

    list = []
    try:
        list_kom_pos = (result.kom_pos).split("| ")
        list_kom_fio = (result.kom_fio).split("| ")
        list_weld_main_material_plate = (
            result.weld_main_material_plate).split("| ")
        list_weld_main_material_tube = (
            result.weld_main_material_tube).split("| ")
    except AttributeError:
        list_kom_pos = ["---", "---", "---", "---"]
        list_kom_fio = ["---", "---", "---", "---"]
        list_weld_main_material_plate = ["---"]
        list_weld_main_material_tube = ["---"]

    list = []
    for i in range(len(list_kom_pos)):
        default = []
        default.append(list_kom_pos[i])
        default.append(list_kom_fio[i])
        list.append(default)

    weld_material = Material_Electrode.objects.all()
    weld_main_material_plate = Material_Plate.objects.all().order_by(
        "thickness", "group_of_material"
    )
    weld_main_material_tube = Material_Tube.objects.all().order_by(
        "diameter", "group_of_material"
    )

    if request.method == "POST":
        list_name_param = [
            "start_date",
            "end_date",
            "welder_material",
            "weld_main_material_plate",
            "weld_main_material_tube",
            "chef_kom_pos",
            "chef_kom_fio",
            "kom_pos",
            "kom_fio",
        ]
        list_param = []
        result = dict(request.POST)

        application = Application.objects.filter(pk=pk).first()
        for i in range(len(list_name_param)):
            name_param = list_name_param[i]
            try:
                param = str(result[name_param])
                param = param[2:-2]
            except KeyError:
                param = "-"
            if param == "":
                param = "---"
            param = param.replace("',", "|")
            param = param.replace("'", "")
            list_param.append(param)

        application.start_date = list_param[0]
        application.end_date = list_param[1]
        application.welder_material = list_param[2]
        application.weld_main_material_plate = list_param[3]
        application.weld_main_material_tube = list_param[4]
        application.chef_kom_pos = list_param[5]
        application.chef_kom_fio = list_param[6]
        application.kom_pos = list_param[7]
        application.kom_fio = list_param[8]
        application.save()
        return redirect("all_applications_confirm")
    return render(
        request,
        "main/application_complete_akt.html",
        {
            "title": title,
            "result": result,
            "list": list,
            "group": group,
            "weld_material": weld_material,
            "weld_main_material_plate": weld_main_material_plate,
            "weld_main_material_tube": weld_main_material_tube,
            "list_weld_main_material_plate": list_weld_main_material_plate,
            "list_weld_main_material_tube": list_weld_main_material_tube,
        },
    )



@login_required(login_url=reverse_lazy("login"))
def application_del(request, pk: int):
    application = get_object_or_404(Application, pk=pk)
    application.delete()
    return redirect("all_applications_give")


@login_required(login_url=reverse_lazy("login"))
def application_confirm(request, pk: int):
    application = get_object_or_404(Application, pk=pk)
    application.aplic_status = Aplic_status.objects.get(aplic_num=2)
    application.save()
    return redirect("all_applications_confirm")


@login_required(login_url=reverse_lazy("login"))
def application_give(request, pk: int):
    application = get_object_or_404(Application, pk=pk)
    application.aplic_status = Aplic_status.objects.get(aplic_num=1)
    application.save()
    return redirect("all_applications_give")


@login_required(login_url=reverse_lazy("login"))
def application_done(request, pk: int):
    application = get_object_or_404(Application, pk=pk)
    application.aplic_status = Aplic_status.objects.get(aplic_num=4)
    application.save()
    return redirect("all_applications_done")


@login_required(login_url=reverse_lazy("login"))
def application_cancel(request, pk: int):
    application = get_object_or_404(Application, pk=pk)
    application.aplic_status = Aplic_status.objects.get(aplic_num=3)
    application.save()
    return redirect("all_applications_cancel")


@login_required(login_url=reverse_lazy("login"))
def pdf_application(request, pk: int):
    result = Application.objects.get(pk=pk).__dict__
    welder_name = (str(result["welder_name"])).split("|")
    welder_brand = (str(result["welder_brand"])).split("|")
    welder_passport = (str(result["welder_passport"])).split("|")
    welder_date_birth = (str(result["welder_date_birth"])).split("|")

    welder_list = []
    for i in range(len(welder_name)):
        default = []
        default.append(i + 1)
        default.append(welder_name[i])
        default.append(welder_brand[i])
        default.append(welder_passport[i])
        default.append(welder_date_birth[i])
        welder_list.append(default)

    result["welder_list"] = welder_list
    result["mas"] = str(result["mas"]).split("|")
    result["gpn"] = str(result["gpn"]).split("|")

    result["sheet_butt_weld_position"] = str(
        result["sheet_butt_weld_position"]
    ).replace("|", ",")
    result["sheet_fillet_weld_position"] = str(
        result["sheet_fillet_weld_position"]
    ).replace("|", ",")
    result["tube_butt_weld_position"] = str(result["tube_butt_weld_position"]).replace(
        "|", ","
    )
    result["tube_fillet_weld_position"] = str(
        result["tube_fillet_weld_position"]
    ).replace("|", ",")
    result["sposob_svarki"] = (
        str(Welding_method.objects.get(id=result["sposob_svarki_id"]).weld_des)
        + " "
        + str(Welding_method.objects.get(id=result["sposob_svarki_id"]).weld_short)
    )

    data = {}
    data = result

    pdf = render_to_pdf("pdf/invoice.html", data)
    return HttpResponse(pdf, content_type="application/pdf")


@login_required(login_url=reverse_lazy("login"))
def pdf_akt(request, pk: int):
    result = Application.objects.get(pk=pk).__dict__
    welder_name = (str(result["welder_name"])).split("|")
    welder_brand = (str(result["welder_brand"])).split("|")
    welder_passport = (str(result["welder_passport"])).split("|")
    welder_date_birth = (str(result["welder_date_birth"])).split("|")

    welder_list = []
    for i in range(len(welder_name)):
        default = []
        default.append(i + 1)
        default.append(welder_name[i])
        default.append(welder_brand[i])
        default.append(welder_passport[i])
        default.append(welder_date_birth[i])
        welder_list.append(default)

    result["start_date"] = datetime.datetime.strptime(
        (result["start_date"]), "%Y-%m-%d"
    ).date()

    result["welder_list"] = welder_list

    result["sposob_svarki"] = (
        str(Welding_method.objects.get(id=result["sposob_svarki_id"]).weld_des)
        + " "
        + str(Welding_method.objects.get(id=result["sposob_svarki_id"]).weld_short)
    )

    result["welder_material"] = result["welder_material"].split(" - ")

    result["mas"] = str(result["mas"]).split("|")
    result["gpn"] = str(result["gpn"]).split("|")

    result["sheet_butt_weld_position"] = str(
        result["sheet_butt_weld_position"]
    ).replace("|", ",")
    result["sheet_fillet_weld_position"] = str(
        result["sheet_fillet_weld_position"]
    ).replace("|", ",")
    result["tube_butt_weld_position"] = str(result["tube_butt_weld_position"]).replace(
        "|", ","
    )
    result["tube_fillet_weld_position"] = str(
        result["tube_fillet_weld_position"]
    ).replace("|", ",")

    list = []
    for i in result["weld_main_material_plate"].split("| "):
        default = []
        list.append(i.split(" - "))

    result["weld_main_material_plate"] = list

    list = []
    for i in result["weld_main_material_tube"].split("| "):
        default = []
        list.append(i.split(" - "))
    result["weld_main_material_tube"] = list

    data = {}
    data = result

    result["kom_pos"] = result["kom_pos"].split("| ")
    result["kom_fio"] = result["kom_fio"].split("| ")
    pdf = render_to_pdf("pdf/pdf_akt.html", data)
    return HttpResponse(pdf, content_type="application/pdf")
