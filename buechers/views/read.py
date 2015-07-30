from books.models import Edition
from buechers.forms import ReadForm
from buechers.functions.lists import update_read_list
from buechers.models import Read
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_protect
from django.utils import timezone

@csrf_protect
@login_required(login_url='/profile/signin/')
def add(request, slug, edition_id):
    edition = get_object_or_404(Edition, book__slug=slug, id=edition_id)
    today = timezone.now()

    if request.method == 'POST':
        form = ReadForm(request.POST)
        if form.is_valid():
            read = form.save()
            update_read_list(read, request.user, edition)
            messages.add_message(request, messages.SUCCESS, 'read successfully addded.')
            return redirect('edition', slug=slug, edition_id=edition_id)
    else:
        form = ReadForm(initial={'user':request.user, 'edition':edition})

    return render(request, 'buecher/buechers/read/form.html', locals())

@csrf_protect
@login_required(login_url='/profile/signin/')
def edit(request, slug, edition_id, read_id):
    edition = get_object_or_404(Edition, book__slug=slug, id=edition_id)
    read = get_object_or_404(Read, id=read_id)
    today = timezone.now()

    if request.method == 'POST':
        form = ReadForm(instance=read, data=request.POST)
        if form.is_valid():
            read = form.save()
            update_read_list(read, request.user, edition)
            messages.add_message(request, messages.SUCCESS, 'read successfully updated.')
            return redirect('edition', slug=slug, edition_id=edition_id)
    else:
        form = ReadForm(instance=read)

    return render(request, 'buecher/buechers/read/form.html', locals())

@csrf_protect
@login_required(login_url='/profile/signin/')
def delete(request, slug, edition_id, read_id):
    edition = get_object_or_404(Edition, book__slug=slug, id=edition_id)
    read = get_object_or_404(Read, id=read_id)

    if request.method == 'POST':
        read.delete()
        messages.add_message(request, messages.SUCCESS, 'read was successfully deleted.')
        return redirect('edition', slug=slug, edition_id=edition_id)
    return render(request, 'buecher/buechers/read/delete.html', locals())
