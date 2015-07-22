import autocomplete_light

from django import forms
from series.models import Series

class SeriesForm(autocomplete_light.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SeriesForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget = forms.TextInput(attrs={'autocomplete':'off', 'class':'form-control'})

    class Meta:
        model = Series
        fields = '__all__'
