from books.forms import BookForm, EBookFileForm, EditionForm
from books.models import Book, EBookFile, Edition, TextFieldSingleLine
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

class EBookFileAdmin(admin.ModelAdmin):
    form = EBookFileForm
    list_display = ('edition', 'ebook')
    list_filter = ('edition__book__series', 'edition__book', 'edition')
    search_fields = ('edition__book__title', 'edition__book__authors__first_name', 'edition__book__authors__last_name', 'edition__book__series__name', 'edition__isbn', 'edition__asin')

    fieldsets = [
        ('edition', {'fields': ['edition']}),
        ('ebook file', {'fields': ['ebook']}),
    ]

class EBookFileInline(admin.StackedInline):
    model = EBookFile
    extra = 1

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

    inlines = [EBookFileInline]

    formfield_overrides = {
        TextFieldSingleLine: {'widget': TextInput(attrs={'autocomplete':'off', 'style':'min-width:50%; '})},
        models.TextField: {'widget': Textarea(attrs={'autocomplete':'off', 'rows':20, 'style':'width: 100%; resize: none;'})},
    }

    fieldsets = [
        ('book', {'fields': ['book']}),
        ('edition', {'fields': ['cover_image', 'isbn', 'asin', 'publisher', 'published_on', 'binding', 'languages']}),
        ('bibtex', {'fields': ['bibtex']}),
        ('links', {'fields': ['links']}),
    ]

    filter_horizontal = ('languages', 'links')

admin.site.register(Book, BookAdmin)
admin.site.register(EBookFile, EBookFileAdmin)
admin.site.register(Edition, EditionAdmin)
