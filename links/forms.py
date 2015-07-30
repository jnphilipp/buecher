import autocomplete_light

from django import forms
from links.models import Link

class LinkForm(autocomplete_light.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LinkForm, self).__init__(*args, **kwargs)
        self.fields['link'].widget = forms.TextInput(attrs={'autocomplete':'off', 'class':'form-control'})

    class Meta:
        model = Link
        fields = ('link',)
