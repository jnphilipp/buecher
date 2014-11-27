from books.models import Book

import autocomplete_light

class BookForm(autocomplete_light.ModelForm):
	class Meta:
		model = Book
		autocomplete_fields = ('binding', 'publisher', 'series')