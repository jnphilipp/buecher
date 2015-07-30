import autocomplete_light

from books.models import Book, EBookFile, Edition
from django import forms

class BookForm(autocomplete_light.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget = forms.TextInput(attrs={'autocomplete':'off', 'class':'form-control'})
        self.fields['volume'].widget = forms.TextInput(attrs={'autocomplete':'off', 'class':'form-control'})

    class Meta:
        model = Book
        fields = ('title', 'authors', 'series', 'volume')

class BookAdminForm(autocomplete_light.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class EBookFileForm(autocomplete_light.ModelForm):
    class Meta:
        model = EBookFile
        fields = '__all__'

class EditionForm(autocomplete_light.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditionForm, self).__init__(*args, **kwargs)
        self.fields['asin'].widget = forms.TextInput(attrs={'autocomplete':'off', 'class':'form-control', 'maxlength':'10'})
        self.fields['isbn'].widget = forms.TextInput(attrs={'autocomplete':'off', 'class':'form-control', 'maxlength':'13'})
        self.fields['published_on'].widget = forms.TextInput(attrs={'autocomplete':'off', 'class':'form-control', 'placeholder':'yyyy-mm-dd'})
        self.fields['bibtex'].widget = forms.Textarea(attrs={'autocomplete':'off', 'class':'form-control', 'style':'resize:none;'})
        self.fields['book'].widget = forms.HiddenInput()

    class Meta:
        model = Edition
        fields = ('book', 'cover_image', 'asin', 'isbn', 'publisher', 'published_on', 'binding', 'languages', 'links', 'bibtex')

class EditionAdminForm(autocomplete_light.ModelForm):
    class Meta:
        model = Edition
        fields = '__all__'
