from books.models import Edition
from buechers.forms import PossessionForm
from buechers.models import Possession, Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

@login_required(login_url='/profile/signin/')
def add(request, slug, edition_id):
    profile = get_object_or_404(Profile, user=request.user)
    edition = get_object_or_404(Edition, book__slug=slug, id=edition_id)
    today = timezone.now()

    if request.method == 'POST':
        form = PossessionForm(request.POST)
        if form.is_valid():
            possession = form.save()
            messages.add_message(request, messages.SUCCESS, 'possession successfully addded.')
            return redirect('edition', slug=slug, edition_id=edition_id)
    else:
        form = PossessionForm(initial={'user':request.user, 'edition':edition, 'unit':profile.default_unit})

    return render(request, 'buecher/buechers/possession/form.html', locals())

@login_required(login_url='/profile/signin/')
def edit(request, slug, edition_id, possession_id):
    edition = get_object_or_404(Edition, book__slug=slug, id=edition_id)
    possession = get_object_or_404(Possession, id=possession_id)

    today = timezone.now()

    if request.method == 'POST':
        form = PossessionForm(instance=possession, data=request.POST)
        if form.is_valid():
            possession = form.save()
            messages.add_message(request, messages.SUCCESS, 'possession successfully updated.')
            return redirect('edition', slug=slug, edition_id=edition_id)
    else:
        form = PossessionForm(instance=possession)

    return render(request, 'buecher/buechers/possession/form.html', locals())
