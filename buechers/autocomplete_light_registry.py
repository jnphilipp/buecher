from buechers.models import List

import autocomplete_light

class Autocomplete(autocomplete_light.AutocompleteModelBase):
    attrs={
        'placeholder': 'choose list',
        'data-autocomplete-minimum-characters': 1,
    }
    widget_attrs={
        'data-widget-maximum-values': 6,
        'class': 'modern-style',
    }

    def choices_for_request(self):
        self.choices = self.choices.filter(user=self.request.user)
        return super(Autocomplete, self).choices_for_request()

    def choice_html(self, choice):
        return self.choice_html_format % (self.choice_value(choice), self.choice_label(choice.name).lower())

autocomplete_light.register(List, Autocomplete, search_fields=['name'], add_another_url_name='person_add_another_create')
