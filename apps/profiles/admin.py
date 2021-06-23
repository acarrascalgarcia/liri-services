from django.contrib import admin

from .forms import ProfileCreationForm, ProfileChangeForm
from .forms import ProfileLabelCreationForm, ProfileLabelChangeForm
from .forms import ProfileCategoryCreationForm, ProfileCategoryChangeForm
from .models import Profile, ProfileLabel, ProfileCategory


class ProfileAdmin(admin.ModelAdmin):
    add_form = ProfileCreationForm
    form = ProfileChangeForm
    model = Profile
    list_display = (
        'uuid',
        'first_name', 'middle_name', 'last_name',
        'user', 'created_at', 'updated_at',
    )
    list_filter = ()
    fieldsets = (
        (
            None, {
                'fields': (
                    'first_name', 'middle_name', 'last_name',
                    'user',
                )
            }
        ),
    )
    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': (
                    'first_name', 'middle_name', 'last_name',
                    'user',
                )
            }
        ),
    )
    search_fields = ('uuid', 'first_name', 'last_name',)
    ordering = ('uuid', 'first_name', 'last_name',)


class ProfileLabelAdmin(admin.ModelAdmin):
    add_form = ProfileLabelCreationForm
    form = ProfileLabelChangeForm
    model = ProfileLabel
    list_display = (
        'uuid', 'profile', 'label',
        'created_at', 'updated_at',
    )
    list_filter = ()
    fieldsets = (
        (
            None, {
                'fields': (
                    'profile', 'label',
                )
            }
        ),
    )
    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': (
                    'profile', 'label',
                )
            }
        ),
    )
    search_fields = ('uuid', 'profile', 'label',)
    ordering = ('uuid', 'profile', 'label',)


class ProfileCategoryAdmin(admin.ModelAdmin):
    add_form = ProfileCategoryCreationForm
    form = ProfileCategoryChangeForm
    model = ProfileCategory
    list_display = (
        'uuid', 'profile', 'category',
        'created_at', 'updated_at',
    )
    list_filter = ()
    fieldsets = (
        (
            None, {
                'fields': (
                    'profile', 'category',
                )
            }
        ),
    )
    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': (
                    'profile', 'category',
                )
            }
        ),
    )
    search_fields = ('uuid', 'profile', 'category',)
    ordering = ('uuid', 'profile', 'category',)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(ProfileLabel, ProfileLabelAdmin)
admin.site.register(ProfileCategory, ProfileCategoryAdmin)
