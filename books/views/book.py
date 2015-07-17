from books.forms import BookForm
from books.models import Book
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

def books(request):
    books = Book.objects.all()
    return render(request, 'buecher/books/book/books.html', locals())

def book(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'buecher/books/book/book.html', locals())

@login_required(login_url='/profile/signin/')
def add(request):
    if request.method == 'POST':
        form = BookForm(data=request.POST)
        if form.is_valid():
            book = form.save()
            messages.add_message(request, messages.SUCCESS, 'book successfully addded.')
            return redirect('book', slug=book.slug)
    else:
        form = BookForm()

    return render(request, 'buecher/books/book/form.html', locals())

@login_required(login_url='/profile/signin/')
def edit(request, slug):
    book = get_object_or_404(Book, slug=slug)

    if request.method == 'POST':
        form = BookForm(instance=book, data=request.POST)
        if form.is_valid():
            book = form.save()
            messages.add_message(request, messages.SUCCESS, 'book successfully updated.')
            return redirect('book', slug=slug)
    else:
        form = BookForm(instance=book)

    return render(request, 'buecher/books/book/form.html', locals())
