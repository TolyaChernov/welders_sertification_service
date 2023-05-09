from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.db.models.query_utils import Q
from django.core.mail import BadHeaderError, send_mail
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import AuthenticationUserForm, RegisterUserForm, RegistrationForm


class RegisterUser(CreateView):
    form_class = RegisterUserForm  # UserCreationForm
    template_name = "users/register.html"
    success_url = reverse_lazy("login")
    # def get_redirect_url(self):
    #     if self.request.method == "POST":
    #         next_url = self.request.POST.get('next')
    #         if next_url != '':
    #             return next_url
    #     return reverse_lazy('home')


class LoginUser(LoginView):
    form_class = AuthenticationUserForm
    template_name = "users/login.html"

    def get_redirect_url(self):
        if self.request.method == "POST":
            next_url = self.request.POST.get("next")
            if next_url != "":
                return next_url
        return reverse_lazy("index")


def logout_user(request):
    logout(request)
    return redirect("index")


#####################################################################


def register(request):
    if not request.user.is_authenticated:
        if request.POST:
            form = RegistrationForm(request.POST or None)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get("username")
                my_password1 = form.cleaned_data.get("password1")
                user = authenticate(username=username, password=my_password1)
                # if user and user.is_active:
                #     login(request, user)
                #     return redirect("private_office")

                # else:
                #     form.add_error(None, "Unknown or disabled account")
                # return render(request, "users/register.html",
                #   {"form": form})
                return redirect("private_office")

            else:
                return render(request, "users/register.html", {"form": form})
        else:
            return render(request, "users/register.html",
                          {"form": RegistrationForm()})
    else:
        return redirect("private_office")


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data["email"]
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "users/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        "domain": "127.0.0.1:8000",
                        "site_name": "Website",
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        "token": default_token_generator.make_token(user),
                        "protocol": "http",
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(
                            subject,
                            email,
                            "admin@example.com",
                            [user.email],
                            fail_silently=False,
                        )
                    except BadHeaderError:
                        return HttpResponse("Invalid header found.")
                    return redirect("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(
        request=request,
        template_name="users/password_reset.html",
        context={"password_reset_form": password_reset_form},
    )
