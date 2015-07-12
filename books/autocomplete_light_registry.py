from books.models import Book, Edition

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

autocomplete_light.register(Book, Autocomplete, search_fields=['title', '^authors__first_name', 'authors__last_name', 'series__name'])
autocomplete_light.register(Edition, Autocomplete, search_fields=['book__title', '^book__authors__first_name', 'book__authors__last_name', 'book__series__name', 'isbn', 'asin'])
