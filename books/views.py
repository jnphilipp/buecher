from books.models import Binding
from books.models import Book
from books.models import EBookFile
from datetime import date
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Sum
from django.shortcuts import get_object_or_404, get_list_or_404, render_to_response

def index(request):
	book_list = Book.objects.all().order_by('-updated_at')
	paginator = Paginator(book_list, 30)

	page = request.GET.get('page')
	try:
		books = paginator.page(page)
	except PageNotAnInteger:
		books = paginator.page(1)
	except EmptyPage:
		books = paginator.page(paginator.num_pages)

	return render_to_response('books/index.html', {'books': books})

def detail(request, book_id):
	book = get_object_or_404(Book, pk=book_id)
	ebook_files = EBookFile.objects.filter(book=book_id)

	next = Book.objects.filter(id__gt=book_id).order_by('id')[:1]
	if next:
		next = next[0]
	previous = Book.objects.filter(id__lt=book_id).order_by('-id')[:1]
	if previous:
		previous = previous[0]

	return render_to_response('books/detail.html', {'book': book, 'ebook_files': ebook_files, 'next': next, 'previous': previous})

def statistics(request):
	statistics = {}
	statistics['book_count'] = Book.objects.count()
	statistics['book_sum'] = Book.objects.aggregate(sum=Sum('price'))
	statistics['book_bindings'] = Book.objects.values('binding__binding').annotate(sum=Sum('price'), count=Count('title')).order_by('binding')

	statistics['purchased_count'] = Book.objects.filter(purchased_on__isnull=False).count()
	statistics['purchased_sum'] = Book.objects.filter(purchased_on__isnull=False).aggregate(sum=Sum('price'))
	statistics['purchased_bindings'] = Book.objects.filter(purchased_on__isnull=False).values('binding__binding').annotate(sum=Sum('price'), count=Count('title')).order_by('binding')

	statistics['sub_count']= Book.objects.filter(purchased_on__isnull=False, read_on__isnull=True).count()
	statistics['sub_sum'] = Book.objects.filter(purchased_on__isnull=False, read_on__isnull=True).aggregate(sum=Sum('price'))
	statistics['sub_bindings'] = Book.objects.filter(purchased_on__isnull=False, read_on__isnull=True).values('binding__binding').annotate(sum=Sum('price'), count=Count('title')).order_by('binding')

	statistics['read_count'] = Book.objects.filter(read_on__isnull=False).count()
	statistics['read_sum'] = Book.objects.filter(read_on__isnull=False).aggregate(sum=Sum('price'))
	statistics['read_bindings'] = Book.objects.filter(read_on__isnull=False).values('binding__binding').annotate(sum=Sum('price'), count=Count('title')).order_by('binding')

	statistics['wishlist_count'] = Book.objects.filter(purchased_on__isnull=True).count()
	statistics['wishlist_sum'] = Book.objects.filter(purchased_on__isnull=True).aggregate(sum=Sum('price'))
	statistics['wishlist_bindings'] = Book.objects.filter(purchased_on__isnull=True).values('binding__binding').annotate(sum=Sum('price'), count=Count('title')).order_by('binding')

	statistics['year_purchased_count'] = Book.objects.filter(purchased_on__isnull=False, purchased_on__year=date.today().year).count()
	statistics['year_purchased_sum'] = Book.objects.filter(purchased_on__isnull=False, purchased_on__year=date.today().year).aggregate(sum=Sum('price'))
	statistics['year_purchased_binding_counts'] = Book.objects.filter(purchased_on__isnull=False, purchased_on__year=date.today().year).values('binding__binding').annotate(sum=Sum('price'), count=Count('title')).order_by('binding')

	statistics['month_purchased_count'] = Book.objects.filter(purchased_on__isnull=False, purchased_on__year=date.today().year, purchased_on__month=date.today().month).count()
	statistics['month_purchased_sum'] = Book.objects.filter(purchased_on__isnull=False, purchased_on__year=date.today().year, purchased_on__month=date.today().month).aggregate(sum=Sum('price'))
	statistics['month_purchased_binding_counts'] = Book.objects.filter(purchased_on__isnull=False, purchased_on__year=date.today().year, purchased_on__month=date.today().month).values('binding__binding').annotate(sum=Sum('price'), count=Count('title')).order_by('binding')

	statistics['year_read_count'] = Book.objects.filter(read_on__isnull=False, read_on__year=date.today().year).count()
	statistics['year_read_sum'] = Book.objects.filter(read_on__isnull=False, read_on__year=date.today().year).aggregate(sum=Sum('price'))
	statistics['year_read_bindings'] = Book.objects.filter(read_on__isnull=False, read_on__year=date.today().year).values('binding__binding').annotate(sum=Sum('price'), count=Count('title')).order_by('binding')

	statistics['month_read_count'] = Book.objects.filter(read_on__isnull=False, read_on__year=date.today().year, read_on__month=date.today().month).count()
	statistics['month_read_sum'] = Book.objects.filter(read_on__isnull=False, read_on__year=date.today().year, read_on__month=date.today().month).aggregate(sum=Sum('price'))
	statistics['month_read_bindings'] = Book.objects.filter(read_on__isnull=False, read_on__year=date.today().year, read_on__month=date.today().month).values('binding__binding').annotate(sum=Sum('price'), count=Count('title')).order_by('binding')

	return render_to_response('books/statistics.html', {'statistics': statistics})