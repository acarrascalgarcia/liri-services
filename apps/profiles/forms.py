from django import forms

from .models import Profile, ProfileLabel, ProfileCategory


class ProfileCreationForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = (
            'first_name', 'middle_name', 'last_name',
            'user',
        )


class ProfileChangeForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = (
            'first_name', 'middle_name', 'last_name',
            'user',
        )


class ProfileLabelCreationForm(forms.ModelForm):

    class Meta:
        model = ProfileLabel
        fields = (
            'profile', 'label',
        )


class ProfileLabelChangeForm(forms.ModelForm):
    
    class Meta:
        model = ProfileLabel
        fields = (
            'profile', 'label',
        )


class ProfileCategoryCreationForm(forms.ModelForm):

    class Meta:
        model = ProfileCategory
        fields = (
            'profile', 'category',
        )


class ProfileCategoryChangeForm(forms.ModelForm):
    
    class Meta:
        model = ProfileCategory
        fields = (
            'profile', 'category',
        )
