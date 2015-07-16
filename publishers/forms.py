import autocomplete_light

from django import forms
from publishers.models import Publisher

class PublisherForm(autocomplete_light.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PublisherForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget = forms.TextInput(attrs={'autocomplete':'off', 'class':'form-control'})

    class Meta:
        model = Publisher
        fields = ('name', 'links')
