from buechers.forms import ListAdminForm, PossessionAdminForm, ReadAdminForm
from buechers.models import List, Possession, Profile, Read, TextFieldSingleLine
from django.contrib import admin
from django.db import models
from django.db.models import Count
from django.forms import TextInput

class ListAdmin(admin.ModelAdmin):
    form = ListAdminForm
    def get_queryset(self, request):
        return List.objects.annotate(book_count=Count('books'))

    def book_count(self, inst):
        return inst.book_count

    formfield_overrides = {
        TextFieldSingleLine: {'widget': TextInput(attrs={'autocomplete':'off', 'style':'min-width:50%; '})},
    }

    list_display = ('name', 'user', 'book_count')
    readonly_fields = ('slug',)
    search_fields = ('name', 'user__username')
    book_count.admin_order_field = 'book_count'
    book_count.short_description = 'Number of Books'

    fieldsets = [
        (None, {'fields': ['user', 'slug', 'name', 'books', 'editions']}),
    ]

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'updated_at')
    search_fields = ('user__username', 'user__first_name', 'user__last_name')

    fieldsets = [
        (None, {'fields': ['user', 'default_unit']}),
    ]

class PossessionAdmin(admin.ModelAdmin):
    form = PossessionAdminForm
    def authors(self, inst):
        return ', '.join([str(a) for a in inst.edition.book.authors.all()])

    def title(self, inst):
        return inst.edition.book.title

    def series(self, inst):
        return inst.edition.book.series

    def volume(self, inst):
        return inst.edition.book.volume

    list_display = ('user', 'title', 'authors', 'series', 'volume', 'acquisition', 'price')
    list_filter = ('edition__book__authors', 'edition__book__series', 'edition__publisher', 'edition__binding', 'edition__languages')
    search_fields = ('edition__book__title', 'edition__book__authors__first_name', 'edition__book__authors__last_name', 'edition__book__series__name', 'edition__isbn', 'edition__asin')

    title.admin_order_field = 'edition__book__title'
    authors.admin_order_field = 'edition__book__authors'
    authors.short_description = 'Authors'
    series.admin_order_field = 'edition__book__series'
    volume.admin_order_field = 'edition__book__volume'

    fieldsets = [
        (None, {'fields': ['user', 'edition', 'acquisition', 'price', 'unit']}),
    ]

class ReadAdmin(admin.ModelAdmin):
    form = ReadAdminForm
    def authors(self, inst):
        return ', '.join([str(a) for a in inst.edition.book.authors.all()])

    def title(self, inst):
        return inst.edition.book.title

    def series(self, inst):
        return inst.edition.book.series

    def volume(self, inst):
        return inst.edition.book.volume

    list_display = ('user', 'title', 'authors', 'series', 'volume', 'started', 'finished')
    list_filter = ('edition__book__authors', 'edition__book__series', 'edition__publisher', 'edition__binding', 'edition__languages')
    search_fields = ('edition__book__title', 'edition__book__authors__first_name', 'edition__book__authors__last_name', 'edition__book__series__name', 'edition__isbn', 'edition__asin')

    title.admin_order_field = 'edition__book__title'
    authors.admin_order_field = 'edition__book__authors'
    authors.short_description = 'Authors'
    series.admin_order_field = 'edition__book__series'
    volume.admin_order_field = 'edition__book__volume'

    fieldsets = [
        (None, {'fields': ['user', 'edition', 'started', 'finished']}),
    ]

admin.site.register(List, ListAdmin)
admin.site.register(Possession, PossessionAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Read, ReadAdmin)
