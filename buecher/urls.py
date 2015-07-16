"""buecher URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

admin.site.site_header = 'buecher administration'

urlpatterns = [
    url(r'^$', 'books.views.book.books', name='home'),

    url(r'^books/book/$', 'books.views.book.books', name='books'),
    url(r'^books/book/(?P<slug>[\w-]+)/$', 'books.views.book.book', name='book'),
    url(r'^books/edition/$', 'books.views.edition.editions', name='editions'),
    url(r'^books/edition/(?P<slug>[\w-]+)/add/$', 'books.views.edition.add', name='edition_add'),
    url(r'^books/edition/(?P<slug>[\w-]+)/(?P<edition_id>\d+)/$', 'books.views.edition.edition', name='edition'),
    url(r'^books/edition/(?P<slug>[\w-]+)/(?P<edition_id>\d+)/edit/$', 'books.views.edition.edit', name='edition_edit'),
    url(r'^books/edition/(?P<slug>[\w-]+)/(?P<edition_id>\d+)/possession/add/$', 'buechers.views.possession.add', name='possession_add'),
    url(r'^books/edition/(?P<slug>[\w-]+)/(?P<edition_id>\d+)/possession/(?P<possession_id>\d+)/edit/$', 'buechers.views.possession.edit', name='possession_edit'),
    url(r'^books/edition/(?P<slug>[\w-]+)/(?P<edition_id>\d+)/read/add/$', 'buechers.views.read.add', name='read_add'),
    url(r'^books/edition/(?P<slug>[\w-]+)/(?P<edition_id>\d+)/read/(?P<read_id>\d+)/edit/$', 'buechers.views.read.edit', name='read_edit'),

    url(r'^persons/person/(?P<slug>[\w-]+)/$', 'persons.views.person', name='person'),
    url(r'^publishers/publisher/(?P<slug>[\w-]+)/$', 'publishers.views.publisher', name='publisher'),

    url(r'^series/series/(?P<slug>[\w-]+)/$', 'series.views.series', name='series'),

    url(r'^api/books/book/$', 'books.views.api.book.books'),
    url(r'^api/books/book/(?P<slug>[\w-]+)/$', 'books.views.api.book.book'),

    url(r'^profile/signin/$', 'buechers.views.base.signin', name='signin'),
    url(r'^profile/signout/$', 'django.contrib.auth.views.logout', name='signout'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
]

if settings.DEBUG:
    urlpatterns.append(url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))
