from books.forms import BookForm, EditionForm
from books.models import Book, Edition, TextFieldSingleLine
from django.contrib import admin
from django.db import models
from django.forms import Textarea, TextInput

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

class BookInline(admin.StackedInline):
    model = Book

class EditionAdmin(admin.ModelAdmin):
    form = EditionForm
    def authors(self, inst):
        return ', '.join([str(a) for a in inst.book.authors.all()])

    def title(self, inst):
        return inst.book.title

    def series(self, inst):
        return inst.book.series

    def volume(self, inst):
        return inst.book.volume

    list_display = ('title', 'authors', 'series', 'volume')
    list_filter = ('book__authors', 'book__series', 'publisher', 'binding', 'languages')
    search_fields = ('book__title', 'book__authors__first_name', 'book__authors__last_name', 'book__series__name', 'isbn', 'asin')

    title.admin_order_field = 'book__title'
    authors.admin_order_field = 'book__authors'
    authors.short_description = 'Authors'
    series.admin_order_field = 'book__series'
    volume.admin_order_field = 'book__volume'

    formfield_overrides = {
        TextFieldSingleLine: {'widget': TextInput(attrs={'autocomplete':'off', 'style':'min-width:50%; '})},
        models.TextField: {'widget': Textarea(attrs={'autocomplete':'off', 'rows':20, 'style':'width: 100%; resize: none;'})},
    }

    fieldsets = [
        ('Book', {'fields': ['book']}),
        ('Edition', {'fields': ['cover_image', 'isbn', 'asin', 'publisher', 'published_on', 'binding', 'languages']}),
        ('Bibtex', {'fields': ['bibtex']}),
        ('Links', {'fields': ['links']}),
    ]

    filter_horizontal = ('languages', 'links')

admin.site.register(Book, BookAdmin)
admin.site.register(Edition, EditionAdmin)
