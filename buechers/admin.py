from buechers.forms import PossessionAdminForm, ReadAdminForm
from buechers.models import Possession, Read
from django.contrib import admin
from django.db import models

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

admin.site.register(Possession, PossessionAdmin)
admin.site.register(Read, ReadAdmin)
