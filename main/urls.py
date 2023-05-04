from django.urls import path
# from drf_yasg import openapi  # new
# from drf_yasg.views import get_schema_view  # new


from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("add_application/", add_application, name="add_application"),
    path("private_office/", private_office, name="private_office"),
    path("test_card/", test_card, name="test_card"),
    # path("all_applications/", all_applications, name="all_applications"),
    path(
        "application/<int:pk>/update/",
        application_update,
        name="application_update"),
    path(
        "application/<int:pk>/complete_akt/",
        application_complete_akt,
        name="application_complete_akt",
    ),
    path("application/<int:pk>/del/", application_del, name="application_del"),
    path("pdf_application/<int:pk>/", pdf_application, name="pdf_application"),
    path("pdf_akt/<int:pk>/", pdf_akt, name="pdf_akt"),
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
]
