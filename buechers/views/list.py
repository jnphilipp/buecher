from books.models import Book, Edition
from buechers.forms import ListForm
from buechers.models import List
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_protect

@login_required(login_url='/profile/signin/')
def lists(request):
    lists = List.objects.filter(user=request.user)
    return render(request, 'buecher/buechers/list/lists.html', locals())

@login_required(login_url='/profile/signin/')
def list(request, slug):
    lst = get_object_or_404(List, slug=slug)
    return render(request, 'buecher/buechers/list/list.html', locals())

@login_required(login_url='/profile/signin/')
@csrf_protect
def add(request):
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            lst = form.save()
            messages.add_message(request, messages.SUCCESS, 'list "%s" successfully addded.' % lst.name.lower())
            return redirect('list', slug=lst.slug)
    else:
        form = ListForm(initial={'user':request.user})

    return render(request, 'buecher/buechers/list/form.html', locals())

@login_required(login_url='/profile/signin/')
@csrf_protect
def delete(request, slug):
    lst = get_object_or_404(List, slug=slug)
    if request.method == 'POST':
        lst.delete()
        messages.add_message(request, messages.SUCCESS, 'list "%s" was successfully deleted.' % lst.name.lower())
        return redirect('lists')
    return render(request, 'buecher/buechers/list/delete.html', locals())

@login_required(login_url='/profile/signin/')
@csrf_protect
def edit(request, slug):
    lst = get_object_or_404(List, slug=slug)

    if request.method == 'POST':
        form = ListForm(instance=lst, data=request.POST)
        if form.is_valid():
            lst = form.save()
            messages.add_message(request, messages.SUCCESS, 'list "%s" successfully updated.' % lst.name.lower())
            return redirect('list', slug=lst.slug)
    else:
        form = ListForm(instance=lst)

    return render(request, 'buecher/buechers/list/form.html', locals())

@login_required(login_url='/profile/signin/')
@csrf_protect
def books_edit(request, slug):
    lst = get_object_or_404(List, slug=slug)
    if request.method == 'POST':
        if 'book' in request.POST:
            book = get_object_or_404(Book, id=request.POST.get('book'))
            lst.books.remove(book)
            lst.save()
    return render(request, 'buecher/buechers/list/books.html', locals())

@login_required(login_url='/profile/signin/')
@csrf_protect
def editions_edit(request, slug):
    lst = get_object_or_404(List, slug=slug)
    if request.method == 'POST':
        if 'edition' in request.POST:
            edition = get_object_or_404(Edition, id=request.POST.get('edition'))
            lst.editions.remove(edition)
            lst.save()
    return render(request, 'buecher/buechers/list/editions.html', locals())
