from books.models import Binding, Publisher, Series

from autocomplete_light import shortcuts as autocomplete_light

autocomplete_light.register(Series,
	search_fields=['name'],
	attrs={
		'placeholder': 'Filter',
		'data-autocomplete-minimum-characters': 1,
	},
	widget_attrs={
		'data-widget-maximum-values': 6,
	},
)

autocomplete_light.register(Publisher,
	search_fields=['name'],
	attrs={
		'placeholder': 'Filter',
		'data-autocomplete-minimum-characters': 1,
	},
	widget_attrs={
		'data-widget-maximum-values': 6,
	},
)

autocomplete_light.register(Binding,
	search_fields=['name'],
	attrs={
		'placeholder': 'Filter',
		'data-autocomplete-minimum-characters': 1,
	},
	widget_attrs={
		'data-widget-maximum-values': 6,
	},
)
