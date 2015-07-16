import autocomplete_light

from buechers.models import Possession, Read

class PossessionForm(autocomplete_light.ModelForm):
    class Meta:
        model = Possession
        fields = '__all__'

class ReadForm(autocomplete_light.ModelForm):
    class Meta:
        model = Read
        fields = '__all__'
