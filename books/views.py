from books.models import Book, Edition
from django.shortcuts import get_object_or_404, redirect, render

def books(request):
    books = Book.objects.all()
    return render(request, 'buecher/books/book/books.html', locals())

def book(request, slug):
    book = get_object_or_404(Book, slug=slug)
    if book.editions.count() == 1:
        return redirect('edition', slug=book.slug, edition_id=book.editions.first().id)
    else:
        return render(request, 'buecher/books/book/book.html', locals())

def edition(request, slug, edition_id):
    edition = get_object_or_404(Edition, book__slug=slug, id=edition_id)
    return render(request, 'buecher/books/edition/edition.html', locals())
