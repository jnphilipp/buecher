import autocomplete_light

from books.models import Book, Edition

class BookForm(autocomplete_light.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class EditionForm(autocomplete_light.ModelForm):
    class Meta:
        model = Edition
        fields = '__all__'
