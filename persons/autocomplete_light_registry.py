from persons.models import Person

import autocomplete_light

class Autocomplete(autocomplete_light.AutocompleteModelBase):
    attrs={
        'placeholder': 'filter',
        'data-autocomplete-minimum-characters': 1,
    }
    widget_attrs={
        'data-widget-maximum-values': 6,
        'class': 'modern-style',
    }

    def choice_html(self, choice):
        return self.choice_html_format % (self.choice_value(choice), self.choice_label(choice).lower())

autocomplete_light.register(Person, Autocomplete, search_fields=['^first_name', 'last_name'], add_another_url_name='person_add_another_create')
