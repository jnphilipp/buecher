from books.models import Binding, Book, EBookFile, Person, Publisher, Series, Url
from datetime import date
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Sum, Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404, render
from operator import attrgetter
import calendar
import json

def books_autocomplete(request):
	if request.is_ajax():
		q = request.GET.get('term', '')
		books = Book.objects.filter(title__icontains=q).distinct('title')[:10]
		results = []
		for book in books:
			book_json = {}
			book_json['id'] = book.id
			book_json['label'] = book.title
			book_json['value'] = book.title
			if not next((True for item in results if item['value'] == book.title), False):
				results.append(book_json)

		persons = Person.objects.filter(Q(firstname__icontains=q) | Q(lastname__icontains=q)).distinct('lastname', 'firstname')[:10]
		for person in persons:
			person_json = {}
			person_json['id'] = person.id
			person_json['label'] = str(person)
			person_json['value'] = str(person)
			if not next((True for item in results if item['value'] == str(person)), False):
				results.append(person_json)

		series = Series.objects.filter(name__icontains=q).distinct('name')[:10]
		for s in series:
			series_json = {}
			series_json['id'] = s.id
			series_json['label'] = s.name
			series_json['value'] = s.name
			if not next((True for item in results if item['value'] == s.name), False):
				results.append(series_json)

		publishers = Publisher.objects.filter(name__icontains=q).distinct('name')[:10]
		for publisher in publishers:
			publisher_json = {}
			publisher_json['id'] = publisher.id
			publisher_json['label'] = publisher.name
			publisher_json['value'] = publisher.name
			if not next((True for item in results if item['value'] == publisher.name), False):
				results.append(publisher_json)

		results = sorted(results, key=lambda result: result['label'])[:10]
		data = json.dumps(results)
	else:
		data = 'fail'

	mimetype = 'application/json'
	return HttpResponse(data, mimetype)


def books(request):
	search = request.GET.get('search') if request.GET.get('search') else ''
	filter = request.GET.get('filter')
	if search or filter:
		firstname, _, lastname = search.rpartition(' ')
		if filter == 'unread':
			book_list = Book.objects.filter((Q(title__icontains=search) | Q(series__name__icontains=search) | (Q(authors__firstname__icontains=firstname) & Q(authors__lastname__icontains=lastname)) | Q(publisher__name__icontains=search)) & Q(read_on__isnull=True)).order_by('authors__lastname', 'authors__firstname', 'series__name', 'volume', 'published_on').distinct()
		elif filter == 'read':
			book_list = Book.objects.filter((Q(title__icontains=search) | Q(series__name__icontains=search) | (Q(authors__firstname__icontains=firstname) & Q(authors__lastname__icontains=lastname)) | Q(publisher__name__icontains=search)) & Q(read_on__isnull=False)).order_by('authors__lastname', 'authors__firstname', 'series__name', 'volume', 'published_on').distinct()
		elif filter == 'wishlist':
			book_list = Book.objects.filter((Q(title__icontains=search) | Q(series__name__icontains=search) | (Q(authors__firstname__icontains=firstname) & Q(authors__lastname__icontains=lastname)) | Q(publisher__name__icontains=search)) & Q(purchased_on__isnull=True)).order_by('authors__lastname', 'authors__firstname', 'series__name', 'volume', 'published_on').distinct()
		elif filter == 'purchased':
			book_list = Book.objects.filter((Q(title__icontains=search) | Q(series__name__icontains=search) | (Q(authors__firstname__icontains=firstname) & Q(authors__lastname__icontains=lastname)) | Q(publisher__name__icontains=search)) & Q(purchased_on__isnull=False)).order_by('authors__lastname', 'authors__firstname', 'series__name', 'volume', 'published_on').distinct()
		else:
			book_list = Book.objects.filter(Q(title__icontains=search) | Q(series__name__icontains=search) | (Q(authors__firstname__icontains=firstname) & Q(authors__lastname__icontains=lastname)) | Q(publisher__name__icontains=search)).order_by('authors__lastname', 'authors__firstname', 'series__name', 'volume', 'published_on').distinct()
	else:
		book_list = Book.objects.all().order_by('-updated_at')

	paginator = Paginator(book_list, 27)
	page = request.GET.get('page')
	try:
		books = paginator.page(page)
	except PageNotAnInteger:
		books = paginator.page(1)
	except EmptyPage:
		books = paginator.page(paginator.num_pages)

	return render(request, 'books/books/books.html', locals())

def book(request, book_id):
	book = get_object_or_404(Book, pk=book_id)
	ebook_files = EBookFile.objects.filter(book=book_id)
	urls = Url.objects.filter(book=book_id)

	return render(request, 'books/books/book.html', {'book': book, 'ebook_files': ebook_files, 'urls': urls})

def publishing_list(request):
	year = request.GET.get('year')
	month = request.GET.get('month')
	purchased = True if request.GET.get('purchased') == 'True' else False
	if month and year:
		month = int(month)
		year = int(year)
		if purchased:
			if month == -1:
				book_list = Book.objects.filter(Q(published_on__year=year)).order_by('series__name', 'volume', 'published_on')
			else:
				book_list = Book.objects.filter(Q(published_on__year=year) & Q(published_on__month=month)).order_by('series__name', 'volume', 'published_on')
		else:
			if month == -1:
				book_list = Book.objects.filter(Q(published_on__year=year) & Q(purchased_on__isnull=True)).order_by('series__name', 'volume', 'published_on')
			else:
				book_list = Book.objects.filter(Q(published_on__year=year) & Q(published_on__month=month) & Q(purchased_on__isnull=True)).order_by('series__name', 'volume', 'published_on')
	else:
		year = date.today().year
		month = date.today().month
		purchased = True
		book_list = Book.objects.filter(Q(published_on__year=year) & Q(published_on__month=month)).order_by('series__name', 'volume', 'published_on')
	paginator = Paginator(book_list, 27)

	page = request.GET.get('page')
	try:
		books = paginator.page(page)
	except PageNotAnInteger:
		books = paginator.page(1)
	except EmptyPage:
		books = paginator.page(paginator.num_pages)

	years = Book.objects.dates('published_on', 'year')
	return render(request, 'books/publishing_list.html', {'books': books, 'months': calendar.month_name[1:], 'selected_month': month, 'years': years, 'selected_year': year, 'selected_purchased': purchased})

def statistics(request):
	statistics = {}
	statistics['book_count'] = Book.objects.count()
	statistics['book_sum'] = Book.objects.aggregate(sum=Sum('price'))
	statistics['book_bindings'] = Book.objects.values('binding__name').annotate(sum=Sum('price'), count=Count('title')).order_by('binding')

	statistics['purchased_count'] = Book.objects.filter(purchased_on__isnull=False).count()
	statistics['purchased_sum'] = Book.objects.filter(purchased_on__isnull=False).aggregate(sum=Sum('price'))
	statistics['purchased_bindings'] = Book.objects.filter(purchased_on__isnull=False).values('binding__name').annotate(sum=Sum('price'), count=Count('title')).order_by('binding')

	statistics['sub_count']= Book.objects.filter(purchased_on__isnull=False, read_on__isnull=True).count()
	statistics['sub_sum'] = Book.objects.filter(purchased_on__isnull=False, read_on__isnull=True).aggregate(sum=Sum('price'))
	statistics['sub_bindings'] = Book.objects.filter(purchased_on__isnull=False, read_on__isnull=True).values('binding__name').annotate(sum=Sum('price'), count=Count('title')).order_by('binding')

	statistics['read_count'] = Book.objects.filter(read_on__isnull=False).count()
	statistics['read_sum'] = Book.objects.filter(read_on__isnull=False).aggregate(sum=Sum('price'))
	statistics['read_bindings'] = Book.objects.filter(read_on__isnull=False).values('binding__name').annotate(sum=Sum('price'), count=Count('title')).order_by('binding')

	statistics['wishlist_count'] = Book.objects.filter(purchased_on__isnull=True).count()
	statistics['wishlist_sum'] = Book.objects.filter(purchased_on__isnull=True).aggregate(sum=Sum('price'))
	statistics['wishlist_bindings'] = Book.objects.filter(purchased_on__isnull=True).values('binding__name').annotate(sum=Sum('price'), count=Count('title')).order_by('binding')

	statistics['year_purchased_count'] = Book.objects.filter(purchased_on__isnull=False, purchased_on__year=date.today().year).count()
	statistics['year_purchased_sum'] = Book.objects.filter(purchased_on__isnull=False, purchased_on__year=date.today().year).aggregate(sum=Sum('price'))
	statistics['year_purchased_binding_counts'] = Book.objects.filter(purchased_on__isnull=False, purchased_on__year=date.today().year).values('binding__name').annotate(sum=Sum('price'), count=Count('title')).order_by('binding')

	statistics['month_purchased_count'] = Book.objects.filter(purchased_on__isnull=False, purchased_on__year=date.today().year, purchased_on__month=date.today().month).count()
	statistics['month_purchased_sum'] = Book.objects.filter(purchased_on__isnull=False, purchased_on__year=date.today().year, purchased_on__month=date.today().month).aggregate(sum=Sum('price'))
	statistics['month_purchased_binding_counts'] = Book.objects.filter(purchased_on__isnull=False, purchased_on__year=date.today().year, purchased_on__month=date.today().month).values('binding__name').annotate(sum=Sum('price'), count=Count('title')).order_by('binding')

	statistics['year_read_count'] = Book.objects.filter(read_on__isnull=False, read_on__year=date.today().year).count()
	statistics['year_read_sum'] = Book.objects.filter(read_on__isnull=False, read_on__year=date.today().year).aggregate(sum=Sum('price'))
	statistics['year_read_bindings'] = Book.objects.filter(read_on__isnull=False, read_on__year=date.today().year).values('binding__name').annotate(sum=Sum('price'), count=Count('title')).order_by('binding')

	statistics['month_read_count'] = Book.objects.filter(read_on__isnull=False, read_on__year=date.today().year, read_on__month=date.today().month).count()
	statistics['month_read_sum'] = Book.objects.filter(read_on__isnull=False, read_on__year=date.today().year, read_on__month=date.today().month).aggregate(sum=Sum('price'))
	statistics['month_read_bindings'] = Book.objects.filter(read_on__isnull=False, read_on__year=date.today().year, read_on__month=date.today().month).values('binding__name').annotate(sum=Sum('price'), count=Count('title')).order_by('binding')

	return render(request, 'books/statistics.html', {'statistics': statistics})