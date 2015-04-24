from books.models import Book, EBookFile, Url
from datetime import date
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
import calendar

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

	paginator = Paginator(book_list, 44)
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

	return render(request, 'books/books/book.html', locals())

def bibtex(request, book_id):
	book = get_object_or_404(Book, pk=book_id)
	return HttpResponse(book.bibtex, content_type='text/plain')

def publishing_list(request):
	selected_year = request.GET.get('year')
	selected_month = request.GET.get('month')
	selected_purchased = True if request.GET.get('purchased') == 'True' else False
	if selected_month and selected_year:
		selected_month = int(selected_month)
		selected_year = int(selected_year)
		if selected_purchased:
			if selected_month == -1:
				book_list = Book.objects.filter(Q(published_on__year=selected_year)).order_by('series__name', 'volume', 'published_on')
			else:
				book_list = Book.objects.filter(Q(published_on__year=selected_year) & Q(published_on__month=selected_month)).order_by('series__name', 'volume', 'published_on')
		else:
			if selected_month == -1:
				book_list = Book.objects.filter(Q(published_on__year=selected_year) & Q(purchased_on__isnull=True)).order_by('series__name', 'volume', 'published_on')
			else:
				book_list = Book.objects.filter(Q(published_on__year=selected_year) & Q(published_on__month=selected_month) & Q(purchased_on__isnull=True)).order_by('series__name', 'volume', 'published_on')
	else:
		selected_year = date.today().year
		selected_month = date.today().month
		selected_purchased = True
		book_list = Book.objects.filter(Q(published_on__year=selected_year) & Q(published_on__month=selected_month)).order_by('series__name', 'volume', 'published_on')
	paginator = Paginator(book_list, 44)

	page = request.GET.get('page')
	try:
		books = paginator.page(page)
	except PageNotAnInteger:
		books = paginator.page(1)
	except EmptyPage:
		books = paginator.page(paginator.num_pages)

	years = Book.objects.dates('published_on', 'year')
	months = calendar.month_name[1:]
	return render(request, 'books/publishing_list.html', locals())