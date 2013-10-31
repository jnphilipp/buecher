from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'books.views.index'),
	url(r'^api/books_autocomplete/', 'books.views.books_autocomplete', name='autocomplete'),
	url(r'^books/$', 'books.views.index'),
	url(r'^books/(?P<book_id>\d+)/$', 'books.views.detail'),
	url(r'^books/publishing_list/$', 'books.views.publishing_list'),
	url(r'^books/publishing_list/(?P<book_id>\d+)/$', 'books.views.publishing_list_detail'),
	url(r'^books/statistics/$', 'books.views.statistics'),
	url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	)