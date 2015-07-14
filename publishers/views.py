from django.shortcuts import get_object_or_404, render
from publishers.models import Publisher

def publisher(request, slug):
    publisher = get_object_or_404(Publisher, slug=slug)
    return render(request, 'buecher/publishers/publisher/publisher.html', locals())
