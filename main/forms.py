from django import forms
from django.forms import ModelForm

from .models import Application


class SearchForm(ModelForm):
    welder_name = forms.CharField(
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-input", "placeholder": "ФИО сварщика"}
        ),
    )

    welder_brand = forms.CharField(
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-input", "placeholder": "Клеймо сварщика"}
        ),
    )

    welder_card_id = forms.CharField(
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-input", "placeholder": "Номер удостоверения"}
        ),
    )

    class Meta:
        model = Application
        fields = [
            "welder_name",
            "welder_brand",
            "welder_card_id",
        ]
