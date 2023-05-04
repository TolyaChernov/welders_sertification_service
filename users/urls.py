from django.contrib.auth.views import (PasswordChangeDoneView,
                                       PasswordChangeView)
from django.urls import path, reverse_lazy

from .forms import PasswordUserChangeForm
from .views import LoginUser, logout_user, register

urlpatterns = [
    path("login/", (LoginUser.as_view()), name="login"),
    path("logout/", logout_user, name="logout"),
    path(
        "change-pass/",
        PasswordChangeView.as_view(
            success_url=reverse_lazy("password_change_done"),
            template_name="users/password_change.html",
            form_class=PasswordUserChangeForm,
        ),
        name="change",
    ),
    path(
        "change-pass-confirm/",
        PasswordChangeDoneView.as_view(
            template_name="users/password_change_success.html"
        ),
        name="password_change_done",
    ),
    ##########################################################################
    # path('personalArea/', personalArea, name='personalArea'),
    path("register/", register, name="register"),
]
