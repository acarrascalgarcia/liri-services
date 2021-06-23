from django.contrib import admin

from .forms import LabelCreationForm, LabelChangeForm
from .forms import TypeCreationForm, TypeChangeForm
from .forms import CategoryCreationForm, CategoryChangeForm
from .models import Label, Type, Category


class LabelAdmin(admin.ModelAdmin):
    add_form = LabelCreationForm
    form = LabelChangeForm
    model = Label
    list_display = (
        'uuid', 'name',
        'created_at', 'updated_at',
    )
    list_filter = ()
    fieldsets = (
        (
            None, {
                'fields': (
                    'name',
                )
            }
        ),
    )
    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': (
                    'name',
                )
            }
        ),
    )
    search_fields = ('uuid', 'name',)
    ordering = ('uuid', 'name',)


class TypeAdmin(admin.ModelAdmin):
    add_form = TypeCreationForm
    form = TypeChangeForm
    model = Type
    list_display = (
        'uuid', 'name',
        'created_at', 'updated_at',
    )
    list_filter = ()
    fieldsets = (
        (
            None, {
                'fields': (
                    'name',
                )
            }
        ),
    )
    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': (
                    'name',
                )
            }
        ),
    )
    search_fields = ('uuid', 'name',)
    ordering = ('uuid', 'name',)


class CategoryAdmin(admin.ModelAdmin):
    add_form = CategoryCreationForm
    form = CategoryChangeForm
    model = Category
    list_display = (
        'uuid', 'name', 'type',
        'created_at', 'updated_at',
    )
    list_filter = ()
    fieldsets = (
        (
            None, {
                'fields': (
                    'name', 'type',
                )
            }
        ),
    )
    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': (
                    'name', 'type',
                )
            }
        ),
    )
    search_fields = ('uuid', 'name',)
    ordering = ('uuid', 'name',)


admin.site.register(Label, LabelAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Category, CategoryAdmin)
