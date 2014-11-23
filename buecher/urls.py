from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'books.views.books'),
	url(r'^api/books_autocomplete/', 'books.views.books_autocomplete', name='autocomplete'),
	url(r'^books/$', 'books.views.books', name='books'),
	url(r'^books/(?P<book_id>\d+)/$', 'books.views.book', name='book'),
	url(r'^books/publishing_list/$', 'books.views.publishing_list', name='publishing_list'),
	url(r'^books/statistics/$', 'books.views.statistics', name='statistics'),
	url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
	urlpatterns += patterns('',
		url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	)