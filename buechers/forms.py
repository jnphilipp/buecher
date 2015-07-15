import autocomplete_light

from buechers.models import Possession

class PossessionForm(autocomplete_light.ModelForm):
    class Meta:
        model = Possession
        fields = '__all__'
