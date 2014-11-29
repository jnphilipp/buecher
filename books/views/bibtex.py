from books.forms import ParseBibTexForm, ParsedBibTexForm
from books.functions import parsers
from books.models import Book, Person, Publisher, Series, Url
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_protect

@csrf_protect
@login_required(login_url='/admin/')
def bibtex(request):
	if request.method == 'POST':
		if '_parse' in request.POST:
			form = ParseBibTexForm(request.POST)
			if form.is_valid():
				entries = parsers.bibtex(form.cleaned_data['bibtex'])
				if len(entries) >= 1:
					messages.add_message(request, messages.SUCCESS, 'Successfully parsed entry from BibTex.')
					e = entries[0]
					form = ParsedBibTexForm(initial={'title':e['title'], 'authors':'\n'.join(str(author) for author in e['authors']), 'series':e['journal'], 'volume':e['volume'], 'publisher':e['publisher'], 'published_on':e['published_on'], 'url':e['url']})
					return render(request, 'books/admin/parsed_bibtex.html', locals())
				else:
					messages.add_message(request, messages.ERROR, 'No entries found.')
					return render(request, 'books/admin/parse_bibtex.html', locals())
			else:
				return render(request, 'books/admin/parse_bibtex.html', locals())
		elif '_create_book' in request.POST:
			form = ParsedBibTexForm(request.POST)
			if form.is_valid():
				series, created = Series.objects.get_or_create(name=form.cleaned_data['series']) if form.cleaned_data['series'] else (None, False)
				publisher, created = Publisher.objects.get_or_create(name=form.cleaned_data['publisher']) if form.cleaned_data['publisher'] else (None, False)
				book = Book()
				book.title = form.cleaned_data['title']
				book.published_on = form.cleaned_data['published_on']
				book.series = series
				book.volume = form.cleaned_data['volume']
				book.publisher = publisher
				book.save()

				authors = form.cleaned_data['authors'].split('\n')
				for author in authors:
					author = eval(author)
					person, created = Person.objects.get_or_create(firstname=author['firstname'], lastname=author['lastname'])
					book.authors.add(person)
				book.save()

				if form.cleaned_data['url']:
					Url.objects.create(url=form.cleaned_data['url'], book=book)

				messages.add_message(request, messages.SUCCESS, 'Successfully created Book from BibTex.')
				return redirect('admin:books_book_change', book.id)
			else:
				messages.add_message(request, messages.ERROR, 'Can not create book.')
				return render(request, 'books/admin/parsed_bibtex.html', locals())
	else:
		form = ParseBibTexForm()
		return render(request, 'books/admin/parse_bibtex.html', locals())