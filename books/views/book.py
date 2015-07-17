from django.shortcuts import get_object_or_404, redirect, render
from books.models import Book

def books(request):
    books = Book.objects.all()
    return render(request, 'buecher/books/book/books.html', locals())

def book(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'buecher/books/book/book.html', locals())
