from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import (AuthenticationForm, PasswordChangeForm,
                                       UserCreationForm)
from django.forms import ValidationError


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "Логин"}),
    )

    email = forms.CharField(
        label="",
        widget=forms.EmailInput(
            attrs={
                "class": "form-input",
                "placeholder": "Email"}),
    )

    password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={"class": "form-input", "placeholder": "Пароль"}
        ),
    )

    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={"class": "form-input", "placeholder": "Пароль еще раз"}
        ),
    )


class AuthenticationUserForm(AuthenticationForm):
    username = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "Логин"}),
    )
    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={"class": "form-input", "placeholder": "Пароль"}
        ),
    )


class PasswordUserChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-input", "placeholder": "Старый пароль"}
        ),
    )
    new_password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={"class": "form-input", "placeholder": "Новый пароль"}
        ),
    )
    new_password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-input",
                "placeholder": "Новый пароль еще раз"}
        ),
    )

    def clean(self):
        cleaned_data = super().clean()
        user = self.user
        new = cleaned_data.get("new_password1")
        if user.check_password(new):
            raise ValidationError("Новый пароль совпадает со старым")


#########################################################


class RegistrationForm(UserCreationForm):
    email = forms.CharField(
        label="",
        widget=forms.EmailInput(
            attrs={
                "class": "form-input",
                "placeholder": "Email"}),
    )
    username = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "Логин"}),
    )
    password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={"class": "form-input", "placeholder": "Новый пароль"}
        ),
    )
    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-input",
                "placeholder": "Новый пароль еще раз"}
        ),
    )
    firstname = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-input", "placeholder": "Номер телефона"}
        ),
    )

    error_messages = {
        "password_mismatch": ("Пароли не совпадают."),
        "error": ("Форма не валидна."),
        "username_exists": ("Пользователь с таким именем уже существует."),
    }

    class Meta:
        model = User
        fields = ("username", "firstname", "email", "password1", "password2")

    def clean_username(self):
        username = self.cleaned_data.get("username")
        try:
            User._default_manager.get(username=username)
            # if the user exists, then let's raise an error message
            raise forms.ValidationError(
                self.error_messages["username_exists"],  # my error message
                code="username_exists",  # set the error message key
            )
        except User.DoesNotExist:
            return username  # if user does not exist so we can continue the registration process

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["firstname"]
        user.password1 = self.cleaned_data["password1"]
        user.password2 = self.cleaned_data["password2"]

        if commit:
            user.save()
        return user
