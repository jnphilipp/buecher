from books.models import Book
from django.forms import CharField, DateField, FloatField, Form, Textarea, TextInput

from autocomplete_light import shortcuts as autocomplete_light

class BookForm(autocomplete_light.ModelForm):
	class Meta:
		model = Book
		autocomplete_fields = ('binding', 'publisher', 'series')
		fields = '__all__'

class ParseBibTexForm(Form):
	bibtex = CharField(widget=Textarea(attrs={'rows':20, 'cols':70, 'style':'resize:none;width:50%;'}), required=True)

class ParsedBibTexForm(Form):
	title = CharField(widget=TextInput(attrs={'style':'width:50%;'}), required=True)
	authors = CharField(widget=Textarea(attrs={'rows':7, 'cols':50, 'style':'resize:none;width:50%;'}), required=False)
	series = CharField(widget=TextInput(attrs={'style':'width:50%;'}), required=False)
	volume = FloatField(widget=TextInput(attrs={'style':'width:50%;'}), required=False)
	publisher = CharField(widget=TextInput(attrs={'style':'width:50%;'}), required=False)
	published_on = DateField(required=False)
	url = CharField(widget=TextInput(attrs={'style':'width:50%;'}), required=False)
	bibtex = CharField(widget=Textarea(attrs={'rows':15, 'cols':50, 'style':'resize:none;width:50%;'}), required=False)
