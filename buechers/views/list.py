from buechers.models import List
from django.shortcuts import get_object_or_404, render

def lists(request):
    lists = List.objects.filter(user=request.user)
    return render(request, 'buecher/buechers/list/list.html', locals())

def list(request, slug):
    lst = get_object_or_404(List, slug=slug)
    return render(request, 'buecher/buechers/list/list.html', locals())
