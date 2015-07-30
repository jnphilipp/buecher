import autocomplete_light

from django import forms
from languages.models import Language

class LanguageForm(autocomplete_light.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LanguageForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget = forms.TextInput(attrs={'autocomplete':'off', 'class':'form-control'})

    class Meta:
        model = Language
        fields = ('name',)
