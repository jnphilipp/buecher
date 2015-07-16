import autocomplete_light

from publishers.models import Publisher

class Autocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields=['name']
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

autocomplete_light.register(Publisher, Autocomplete, add_another_url_name='publisher_add_another_create')
