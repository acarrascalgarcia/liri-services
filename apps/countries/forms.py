from django import forms

from .models import Currency, Country


class CurrencyCreationForm(forms.ModelForm):

    class Meta:
        model = Currency
        fields = (
            'code', 'symbol',
            'name', 'english_name',
        )


class CurrencyChangeForm(forms.ModelForm):

    class Meta:
        model = Currency
        fields = (
            'code', 'symbol',
            'name', 'english_name',
        )


class CountryCreationForm(forms.ModelForm):

    class Meta:
        model = Country
        fields = (
            'code', 'name', 'english_name',
            'currency', 'flag_url',
        )


class CountryChangeForm(forms.ModelForm):

    class Meta:
        model = Country
        fields = (
            'code', 'name', 'english_name',
            'currency', 'flag_url',
        )
