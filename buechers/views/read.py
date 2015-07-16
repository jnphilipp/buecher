from books.models import Edition
from buechers.forms import ReadForm
from buechers.models import Read
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

@login_required(login_url='/profile/signin/')
def add(request, slug, edition_id):
    edition = get_object_or_404(Edition, book__slug=slug, id=edition_id)
    today = timezone.now()

    if request.method == 'POST':
        form = ReadForm(request.POST)
        if form.is_valid():
            read = form.save()
            messages.add_message(request, messages.SUCCESS, 'the read successfully addded.')
            return redirect('edition', slug=slug, edition_id=edition_id)
    else:
        form = ReadForm(initial={'user':request.user, 'edition':edition})

    return render(request, 'buecher/buechers/read/form.html', locals())

@login_required(login_url='/profile/signin/')
def edit(request, slug, edition_id, read_id):
    edition = get_object_or_404(Edition, book__slug=slug, id=edition_id)
    read = get_object_or_404(Read, id=read_id)

    today = timezone.now()

    if request.method == 'POST':
        form = ReadForm(instance=read, data=request.POST)
        if form.is_valid():
            read = form.save()
            messages.add_message(request, messages.SUCCESS, 'the read successfully addded.')
            return redirect('edition', slug=slug, edition_id=edition_id)
    else:
        form = ReadForm(instance=read)

    return render(request, 'buecher/buechers/read/form.html', locals())
