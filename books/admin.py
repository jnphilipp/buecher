from books.models import Binding, Book, EBookFile, Language, Person, Publisher, Series, Url
from django.contrib import admin
from django.forms import TextInput
from django.db import models

class PersonAdmin(admin.ModelAdmin):
	search_fields = ('firstname', 'lastname')

	formfield_overrides = {
		models.TextField: {'widget': TextInput(attrs={'size':'50', 'autocomplete':'off'})},
	}

	fieldsets = [
		(None, {'fields': ['firstname', 'lastname']}),
	]

class PublisherAdmin(admin.ModelAdmin):
	search_fields = ('name',)

	formfield_overrides = {
		models.TextField: {'widget': TextInput(attrs={'size':'50', 'autocomplete':'off'})},
	}

	fieldsets = [
		(None, {'fields': ['name']}),
	]

class BindingAdmin(admin.ModelAdmin):
	formfield_overrides = {
		models.TextField: {'widget': TextInput(attrs={'size':'50', 'autocomplete':'off'})},
	}

	fieldsets = [
		(None, {'fields': ['binding']}),
	]

class LanguageAdmin(admin.ModelAdmin):
	formfield_overrides = {
		models.TextField: {'widget': TextInput(attrs={'size':'50', 'autocomplete':'off'})},
	}

	fieldsets = [
		(None, {'fields': ['language']}),
	]

class SeriesAdmin(admin.ModelAdmin):
	search_fields = ('name',)

	formfield_overrides = {
		models.TextField: {'widget': TextInput(attrs={'size':'50', 'autocomplete':'off'})},
	}

	fieldsets = [
		(None, {'fields': ['name']}),
	]

class EBookFileAdmin(admin.ModelAdmin):
	fieldsets = [
		('E-Book File', {'fields': ['ebook_file']}),
		('Book', {'fields': ['book']})
	]

class EBookFileInline(admin.StackedInline):
	model = EBookFile
	extra = 1

class UrlAdmin(admin.ModelAdmin):
	formfield_overrides = {
		models.TextField: {'widget': TextInput(attrs={'size':'50', 'autocomplete':'off'})},
	}

	fieldsets = [
		(None, {'fields': ['url']}),
		('Book', {'fields': ['book']})
	]

class UrlInline(admin.StackedInline):
	formfield_overrides = {
		models.TextField: {'widget': TextInput(attrs={'size':'50', 'autocomplete':'off'})},
	}

	model = Url
	extra = 1

class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'get_authors', 'series', 'volume', 'show_link')
	ordering = ('-updated_at',)

	formfield_overrides = {
		models.CharField: {'widget': TextInput(attrs={'size':'50', 'autocomplete':'off'})},
		models.FloatField: {'widget': TextInput(attrs={'size':'50', 'autocomplete':'off'})},
		models.TextField: {'widget': TextInput(attrs={'size':'100', 'autocomplete':'off'})},
		models.DateField: {'widget': admin.widgets.AdminDateWidget(attrs={'size':'50', 'autocomplete':'off'})},
	}

	fieldsets = [
		(None, {'fields': ['title', 'authors']}),
		('Series details', {'fields': ['series', 'volume']}),
		('Edition details', {'fields': ['isbn', 'asin', 'publisher', 'published_on', 'binding', 'languages', 'price', 'cover_image']}),
		('Details', {'fields': ['purchased_on', 'read_on']}),
	]
	inlines = [EBookFileInline, UrlInline]
	filter_horizontal = ('authors', 'languages')

	def show_link(self, obj):
		return '<a href="%s">view</a>' % obj.get_absolute_url()
	show_link.allow_tags = True

admin.site.register(Binding, BindingAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(EBookFile, EBookFileAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Url, UrlAdmin)