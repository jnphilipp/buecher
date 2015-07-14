from books.models import Book
from django.http import HttpResponse, HttpResponseNotFound
from django.utils import timezone
from json import dumps

def books(request):
    """Handels GET/POST request to export books.
    """
    books = Book.objects.all()
    data = {'timestamp':timezone.now().strftime('%Y-%m-%dT%H:%M:%S:%f%z'),
            'books':[book.to_json() for book in books]}
    return HttpResponse(dumps(data), 'application/json')

def book(request, slug):
    """Handels GET/POST request to export the given book.
    """
    try:
        book = Book.objects.get(slug=slug)
        data = {'timestamp':timezone.now().strftime('%Y-%m-%dT%H:%M:%S:%f%z'),
                'books':[book.to_json()]}
        return HttpResponse(dumps(data), 'application/json')
    except Book.DoesNotExist:
        return HttpResponseNotFound('Book with slug "%s" not found.' % slug)
