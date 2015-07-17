from buechers.forms import UserChangeForm
from buechers.models import Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_protect
from units.models import Unit

@login_required(login_url='profile/signin/')
@csrf_protect
def profile(request):
    if request.method == 'POST':
        form = UserChangeForm(instance=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            profile = get_object_or_404(Profile, user=user)
            profile.default_unit = get_object_or_404(Unit, id=form.cleaned_data['default_unit'])
            profile.save()
            messages.success(request, 'your profile has been successfully updated.')
    else:
        profile = get_object_or_404(Profile, user=request.user)
        form = UserChangeForm(instance=request.user, initial={'default_unit':profile.default_unit.id if profile.default_unit else None})

    return render(request, 'buecher/buechers/profile/form.html', locals())
