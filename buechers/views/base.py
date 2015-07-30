from buechers.forms import AuthenticationForm, UserCreationForm
from buechers.models import List, Profile
from django.contrib import messages
from django.contrib.auth import authenticate, login, views
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def signin(request):
    gnext = request.GET.get('next')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, 'you have successfully signed in.')

                return redirect(gnext) if gnext else redirect('home')
            else:
                messages.add_message(request, messages.ERROR, 'your account is disabled.')
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.add_message(request, messages.ERROR, 'please enter a correct username and password to sign in. Note that both fields may be case-sensitive.')
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        form = AuthenticationForm(request)
        return render(request, 'registration/login.html', locals())

@csrf_protect
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()

            Profile.objects.create(user=new_user)
            List.objects.create(user=new_user, name='read books')
            List.objects.create(user=new_user, name='reading books')
            List.objects.create(user=new_user, name='unread books')
            List.objects.create(user=new_user, name='whishlist')

            messages.info(request, 'thanks for signing up. you are now logged in.')
            new_user = authenticate(username=request.POST['username'], password=request.POST['password1'])
            login(request, new_user)
            return redirect('profile')
        else:
            return render(request, 'registration/signup.html', locals())
    else:
        form = UserCreationForm()
        return render(request, 'registration/signup.html', locals())

@csrf_protect
def password_reset_confirm(request, uidb64=None, token=None):
    return views.password_reset_confirm(request, uidb64=uidb64, token=token, post_reset_redirect=reverse('signin'))

@csrf_protect
def password_reset(request):
    return views.password_reset(request, post_reset_redirect=reverse('signin'))
