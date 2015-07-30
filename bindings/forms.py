import autocomplete_light

from django import forms
from bindings.models import Binding

class BindingForm(autocomplete_light.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BindingForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget = forms.TextInput(attrs={'autocomplete':'off', 'class':'form-control'})

    class Meta:
        model = Binding
        fields = ('name',)
