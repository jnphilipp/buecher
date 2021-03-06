from books.forms import BookForm
from books.models import Binding, Book, EBookFile, Language, Person, Publisher, Series, Url, TextFieldSingleLine
from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

class PersonAdmin(admin.ModelAdmin):
	list_display = ('lastname', 'firstname')
	search_fields = ('firstname', 'lastname')

	formfield_overrides = {
		TextFieldSingleLine: {'widget': TextInput(attrs={'autocomplete':'off'})},
	}

	fieldsets = [
		(None, {'fields': ['firstname', 'lastname']}),
	]

class PublisherAdmin(admin.ModelAdmin):
	search_fields = ('name',)

	formfield_overrides = {
		TextFieldSingleLine: {'widget': TextInput(attrs={'autocomplete':'off'})},
	}

	fieldsets = [
		(None, {'fields': ['name']}),
	]

class BindingAdmin(admin.ModelAdmin):
	formfield_overrides = {
		TextFieldSingleLine: {'widget': TextInput(attrs={'autocomplete':'off'})},
	}

	fieldsets = [
		(None, {'fields': ['name']}),
	]

class LanguageAdmin(admin.ModelAdmin):
	formfield_overrides = {
		TextFieldSingleLine: {'widget': TextInput(attrs={'autocomplete':'off'})},
	}

	fieldsets = [
		(None, {'fields': ['name']}),
	]

class SeriesAdmin(admin.ModelAdmin):
	search_fields = ('name',)

	formfield_overrides = {
		TextFieldSingleLine: {'widget': TextInput(attrs={'autocomplete':'off'})},
	}

	fieldsets = [
		(None, {'fields': ['name']}),
	]

class EBookFileAdmin(admin.ModelAdmin):
	list_display = ('filename', 'book')
	fieldsets = [
		('E-Book File', {'fields': ['ebook_file']}),
		('Book', {'fields': ['book']})
	]

class EBookFileInline(admin.StackedInline):
	model = EBookFile
	extra = 1

class UrlAdmin(admin.ModelAdmin):
	formfield_overrides = {
		TextFieldSingleLine: {'widget': TextInput(attrs={'autocomplete':'off'})},
	}

	fieldsets = [
		(None, {'fields': ['url']}),
		('Book', {'fields': ['book']})
	]

class UrlInline(admin.StackedInline):
	formfield_overrides = {
		TextFieldSingleLine: {'widget': TextInput(attrs={'autocomplete':'off'})},
	}

	model = Url
	extra = 1

class BookAdmin(admin.ModelAdmin):
	def show_link(self, obj):
		return '<a href="%s"><i class="icon-eye-open icon-alpha75"></i>View on site</a>' % obj.get_absolute_url()

	form = BookForm
	list_display = ('title', 'get_authors', 'series', 'volume', 'show_link')
	search_fields = ('title',)
	list_filter = ('authors', 'series')
	ordering = ('-updated_at',)
	show_link.allow_tags = True
	show_link.short_description = 'View on site'

	formfield_overrides = {
		models.CharField: {'widget': TextInput(attrs={'autocomplete':'off'})},
		models.FloatField: {'widget': TextInput(attrs={'autocomplete':'off'})},
		TextFieldSingleLine: {'widget': TextInput(attrs={'autocomplete':'off', 'style':'width:50%;'})},
		models.DateField: {'widget': admin.widgets.AdminDateWidget(attrs={'autocomplete':'off'})},
		models.TextField: {'widget': Textarea(attrs={'autocomplete':'off', 'style':'resize:none;width:50%;', 'rows':15, 'cols':100})},
	}

	fieldsets = [
		(None, {'fields': ['title', 'authors']}),
		('Series details', {'fields': ['series', 'volume']}),
		('Edition details', {'fields': ['isbn', 'asin', 'publisher', 'published_on', 'binding', 'languages', 'price', 'cover_image', 'bibtex']}),
		('Details', {'fields': ['purchased_on', 'read_on']}),
	]
	inlines = [EBookFileInline, UrlInline]
	filter_horizontal = ('authors', 'languages')

admin.site.register(Binding, BindingAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(EBookFile, EBookFileAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Url, UrlAdmin)