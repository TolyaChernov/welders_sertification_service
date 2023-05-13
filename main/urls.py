from django.urls import path

from .views import *

# from drf_yasg import openapi  # new
# from drf_yasg.views import get_schema_view  # new


urlpatterns = [
    path("", index, name="index"),
    path("add_application/", add_application, name="add_application"),
    path("private_office/", private_office, name="private_office"),
    path(
        "application/<int:pk>/update/",
        application_update,
        name="application_update"),
    path(
        "application/<int:pk>/complete_akt/",
        application_complete_akt,
        name="application_complete_akt",
    ),
    path(
        "application_complete_protokol/<int:pk>/",
        application_complete_protokol,
        name="application_complete_protokol",
    ),
    path("application/<int:pk>/del/", application_del, name="application_del"),
    path("pdf_application/<int:pk>/", pdf_application, name="pdf_application"),
    path("pdf_akt/<int:pk>/", pdf_akt, name="pdf_akt"),
    path("pdf_protokol/<int:pk>/", pdf_protokol, name="pdf_protokol"),
    path(
        "all_applications_give/",
        all_applications_give,
        name="all_applications_give"),
    path(
        "all_applications_confirm/",
        all_applications_confirm,
        name="all_applications_confirm",
    ),
    path(
        "all_applications_done/",
        all_applications_done,
        name="all_applications_done"),
    path(
        "all_applications_cancel/",
        all_applications_cancel,
        name="all_applications_cancel",
    ),
    path(
        "application_confirm/<int:pk>/", application_confirm, name="application_confirm"
    ),
    path(
        "application_give/<int:pk>/",
        application_give,
        name="application_give"),
    path(
        "application_done/<int:pk>/",
        application_done,
        name="application_done"),
    path(
        "application_cancel/<int:pk>/",
        application_cancel,
        name="application_cancel"),
    path("all_materials/", all_materials, name="all_materials"),
    path("material_plate/", material_plate, name="material_plate"),
    path("material_tube/", material_tube, name="material_tube"),
    path("material_wire/", material_wire, name="material_wire"),
    path("material_rod/", material_rod, name="material_rod"),
    path("material_electrode/", material_electrode, name="material_electrode"),
]
