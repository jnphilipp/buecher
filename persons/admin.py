from django.contrib import admin
from django.forms import TextInput
from persons.models import Person, TextFieldSingleLine

class PersonAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'updated_at')
    list_filter = ('links', )
    readonly_fields = ('slug',)
    search_fields = ('first_name', 'last_name')

    formfield_overrides = {
        TextFieldSingleLine: {'widget': TextInput(attrs={'autocomplete':'off'})},
    }

    fieldsets = [
        (None, {'fields': ['slug', 'first_name', 'last_name']}),
        ('links', {'fields': ['links']}),
    ]

    filter_horizontal = ('links',)

admin.site.register(Person, PersonAdmin)
