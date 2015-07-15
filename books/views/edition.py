from books.models import Edition
from buechers.models import Possession
from django.shortcuts import get_object_or_404, render

def editions(request):
    editions = Edition.objects.all()
    return render(request, 'buecher/books/edition/editions.html', locals())

def edition(request, slug, edition_id):
    edition = get_object_or_404(Edition, book__slug=slug, id=edition_id)
    possessions = Possession.objects.filter(user=request.user).filter(edition=edition)
    return render(request, 'buecher/books/edition/edition.html', locals())
