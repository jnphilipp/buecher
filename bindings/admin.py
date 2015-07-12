from django.contrib import admin
from django.forms import TextInput
from bindings.models import Binding, TextFieldSingleLine

class BindingAdmin(admin.ModelAdmin):
    list_display = ('name', 'updated_at')
    readonly_fields = ('slug',)
    search_fields = ('name',)

    formfield_overrides = {
        TextFieldSingleLine: {'widget': TextInput(attrs={'autocomplete':'off'})},
    }

    fieldsets = [
        (None, {'fields': ['slug', 'name']}),
    ]

admin.site.register(Binding, BindingAdmin)
