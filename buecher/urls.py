from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'books.views.books.books', name='home'),
	url(r'^api/search/autocomplete/', 'books.views.api.search_autocomplete', name='search_autocomplete'),
	url(r'^books/$', 'books.views.books.books', name='books'),
	url(r'^books/(?P<book_id>\d+)/$', 'books.views.books.book', name='book'),
	url(r'^books/(?P<book_id>\d+)/bibtex/$', 'books.views.books.bibtex', name='book_bibtex'),
	url(r'^books/publishing_list/$', 'books.views.books.publishing_list', name='publishing_list'),
	url(r'^books/statistics/$', 'books.views.statistics.statistics', name='statistics'),
	url(r'^admin/books/bibtex/$', 'books.views.bibtex.bibtex', name='bibtex'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^autocomplete/', include('autocomplete_light.urls')),
)

if settings.DEBUG:
	urlpatterns += patterns('',
		url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	)
