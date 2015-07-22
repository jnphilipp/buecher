from books.models import Book, Edition
from django.shortcuts import render

def statistics(request):
    books = Book.objects.all().count()
    editions = Edition.objects.all().count()
    return render(request, 'buecher/buechers/statistics.html', locals())
