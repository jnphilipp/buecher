import autocomplete_light

from books.models import Book

class BookForm(autocomplete_light.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
