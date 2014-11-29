from books.models import Book
from django.db.models import Count, Sum
from django.shortcuts import redirect, render
from datetime import date

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