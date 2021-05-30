from django.contrib import admin

from .forms import CurrencyCreationForm, CurrencyChangeForm
from .forms import CountryCreationForm, CountryChangeForm
from .models import Currency, Country


class CurrencyAdmin(admin.ModelAdmin):
    add_form = CurrencyCreationForm
    form = CurrencyChangeForm
    model = Currency
    list_display = (
        'code', 'symbol',
        'name', 'english_name',
    )
    list_filter = ()
    fieldsets = (
        (
            None, {
                'fields': (
                    'code', 'symbol',
                    'name', 'english_name',
                )
            }
        ),
    )
    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': (
                    'code', 'symbol',
                    'name', 'english_name',
                )
            }
        ),
    )
    search_fields = ('code', 'name',)
    ordering = ('code', 'name',)


class CountryAdmin(admin.ModelAdmin):
    add_form = CountryCreationForm
    form = CountryChangeForm
    model = Country
    list_display = (
        'code', 'name', 'english_name',
        'currency', 'flag_url'
    )
    list_filter = ()
    fieldsets = (
        (
            None, {
                'fields': (
                    'code', 'name', 'english_name',
                    'currency', 'flag_url'
                )
            }
        ),
    )
    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': (
                    'code', 'name', 'english_name',
                    'currency', 'flag_url'
                )
            }
        ),
    )
    search_fields = ('code', 'name',)
    ordering = ('code', 'name',)


admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Country, CountryAdmin)
