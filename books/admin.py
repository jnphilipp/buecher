from books.forms import BookForm
from books.models import Book, TextFieldSingleLine
from django.contrib import admin
from django.db import models
from django.forms import TextInput

class BookAdmin(admin.ModelAdmin):
    form = BookForm
    def get_authors(self, inst):
        return ', '.join([str(a) for a in inst.authors.all()])

    list_display = ('title', 'get_authors', 'series', 'volume')
    list_filter = ('authors', 'series')
    readonly_fields = ('slug',)
    search_fields = ('title', 'authors__first_name', 'authors__last_name', 'series__name')

    get_authors.admin_order_field = 'authors'
    get_authors.short_description = 'Authors'

    formfield_overrides = {
        TextFieldSingleLine: {'widget': TextInput(attrs={'autocomplete':'off', 'style':'min-width:50%; '})},
    }

    fieldsets = [
        (None, {'fields': ['slug', 'title', 'authors']}),
        ('series', {'fields': ['series', 'volume']}),
    ]

    filter_horizontal = ('authors',)

admin.site.register(Book, BookAdmin)
