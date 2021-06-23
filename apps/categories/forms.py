from django import forms

from .models import Label, Type, Category


class LabelCreationForm(forms.ModelForm):

    class Meta:
        model = Label
        fields = (
            'name',
        )


class LabelChangeForm(forms.ModelForm):
    
    class Meta:
        model = Label
        fields = (
            'name',
        )


class TypeCreationForm(forms.ModelForm):

    class Meta:
        model = Type
        fields = (
            'name',
        )


class TypeChangeForm(forms.ModelForm):
    
    class Meta:
        model = Type
        fields = (
            'name',
        )


class CategoryCreationForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = (
            'name', 'type',
        )


class CategoryChangeForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = (
            'name', 'type',
        )
