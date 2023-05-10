from django.contrib.auth import views as auth_views  # import this
from django.contrib.auth.views import (PasswordChangeDoneView, PasswordChangeView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView)
from django.urls import path, reverse_lazy

from .forms import PasswordUserChangeForm
from .views import LoginUser, logout_user, register
from .forms import AuthenticationUserForm, RegisterUserForm, RegistrationForm, ResetPasswordUserForm, SetPasswordUserForm
# from .views import MyLoginView, RegisterView


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
    path("register/", register, name="register"),
    path(
        "password-reset/",
        PasswordResetView.as_view(template_name="users/password_reset.html", 
        form_class = ResetPasswordUserForm, success_url=reverse_lazy('password_reset_done'),),
        name="password-reset",
    ),
    path(
        "password-reset/done/",
        PasswordResetDoneView.as_view(
            template_name="users/password_reset_done.html"),
        name="password_reset_done",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html", form_class = SetPasswordUserForm
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complete/",
        PasswordResetCompleteView.as_view(
            template_name="users/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    # path("password_reset", password_reset_request, name="password_reset"),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='main/password/password_reset_done.html'), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="main/password/password_reset_confirm.html"), name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='main/password/password_reset_complete.html'), name='password_reset_complete'),
]
