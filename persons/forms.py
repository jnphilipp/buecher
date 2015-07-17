import autocomplete_light

from django import forms
from persons.models import Person

class PersonForm(autocomplete_light.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget = forms.TextInput(attrs={'autocomplete':'off', 'class':'form-control'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'autocomplete':'off', 'class':'form-control'})

    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'links')
