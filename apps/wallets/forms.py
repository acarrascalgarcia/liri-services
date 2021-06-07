from django import forms

from .models import Entity, Wallet


class EntityCreationForm(forms.ModelForm):

    class Meta:
        model = Entity
        fields = (
            'name', 'code', 'country',
        )


class EntityChangeForm(forms.ModelForm):

    class Meta:
        model = Entity
        fields = (
            'name', 'code', 'country',
        )


class WalletCreationForm(forms.ModelForm):

    class Meta:
        model = Wallet
        fields = (
            'name', 'entity', 'currency',
        )


class WalletChangeForm(forms.ModelForm):

    class Meta:
        model = Wallet
        fields = (
            'name', 'entity', 'currency',
        )
