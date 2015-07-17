from books.forms import EditionForm
from books.models import Book, Edition
from buechers.models import Possession, Read
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

def editions(request):
    editions = Edition.objects.all()
    return render(request, 'buecher/books/edition/editions.html', locals())

def edition(request, slug, edition_id):
    edition = get_object_or_404(Edition, book__slug=slug, id=edition_id)
    return render(request, 'buecher/books/edition/edition.html', locals())

@login_required(login_url='/profile/signin/')
def add(request, slug):
    book = get_object_or_404(Book, slug=slug)
    today = timezone.now()

    if request.method == 'POST':
        form = EditionForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            edition = form.save()
            messages.add_message(request, messages.SUCCESS, 'edition successfully addded.')
            return redirect('edition', slug=slug, edition_id=edition.id)
    else:
        form = EditionForm(initial={'book':book})

    return render(request, 'buecher/books/edition/form.html', locals())

@login_required(login_url='/profile/signin/')
def edit(request, slug, edition_id):
    book = get_object_or_404(Book, slug=slug)
    edition = get_object_or_404(Edition, book=book, id=edition_id)
    today = timezone.now()

    if request.method == 'POST':
        form = EditionForm(instance=edition, data=request.POST, files=request.FILES)
        if form.is_valid():
            edition = form.save()
            messages.add_message(request, messages.SUCCESS, 'edition successfully updated.')
            return redirect('edition', slug=slug, edition_id=edition_id)
    else:
        form = EditionForm(instance=edition)

    return render(request, 'buecher/books/edition/form.html', locals())
