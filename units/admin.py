from units.models import Unit, TextFieldSingleLine
from django.contrib import admin
from django.forms import TextInput
from django.db import models

class UnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol', 'precision')
    readonly_fields = ('slug',)
    search_fields = ('name', 'symbol')

    formfield_overrides = {
        TextFieldSingleLine: {'widget': TextInput(attrs={'autocomplete':'off'})},
    }

    fieldsets = [
        (None, {'fields': ['slug', 'name', 'symbol', 'precision']}),
    ]

admin.site.register(Unit, UnitAdmin)
