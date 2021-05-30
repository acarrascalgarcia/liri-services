from django.contrib import admin

from .forms import ProfileCreationForm, ProfileChangeForm
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    add_form = ProfileCreationForm
    form = ProfileChangeForm
    model = Profile
    list_display = (
        'uuid',
        'first_name', 'middle_name', 'last_name',
<<<<<<< HEAD
        'user', 'created_at', 'updated_at',
=======
        'user',
>>>>>>> 4b6ed126233285efef0f86abd3ff9e8b1ab2988f
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


admin.site.register(Profile, ProfileAdmin)
