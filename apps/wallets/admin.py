from django.contrib import admin

from .forms import EntityCreationForm, EntityChangeForm
from .forms import WalletCreationForm, WalletChangeForm
from .models import Entity, Wallet


class EntityAdmin(admin.ModelAdmin):
    add_form = EntityCreationForm
    form = EntityChangeForm
    model = Entity
    list_display = (
        'uuid', 'name', 'code', 'country',
        'created_at', 'updated_at',
    )
    list_filter = ()
    fieldsets = (
        (
            None, {
                'fields': (
                    'name', 'code', 'country',
                )
            }
        ),
    )
    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': (
                   'name', 'code', 'country',
                )
            }
        ),
    )
    search_fields = ('uuid', 'name', 'code',)
    ordering = ('uuid', 'name', 'code',)


class WalletAdmin(admin.ModelAdmin):
    add_form = WalletCreationForm
    form = WalletChangeForm
    model = Wallet
    list_display = (
        'uuid', 'name', 'entity', 'currency',
        'created_at', 'updated_at',
    )
    list_filter = ()
    fieldsets = (
        (
            None, {
                'fields': (
                    'name', 'entity', 'currency',
                )
            }
        ),
    )
    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': (
                   'name', 'entity', 'currency',
                )
            }
        ),
    )
    search_fields = ('uuid', 'name',)
    ordering = ('uuid', 'name',)


admin.site.register(Entity, EntityAdmin)
admin.site.register(Wallet, WalletAdmin)
