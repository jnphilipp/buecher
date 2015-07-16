from books.models import Edition
from buechers.models import Possession, Read
from django.shortcuts import get_object_or_404, render

def editions(request):
    editions = Edition.objects.all()
    return render(request, 'buecher/books/edition/editions.html', locals())

def edition(request, slug, edition_id):
    edition = get_object_or_404(Edition, book__slug=slug, id=edition_id)

    if not request.user.is_anonymous():
        possessions = Possession.objects.filter(user=request.user).filter(edition=edition)
        reads = Read.objects.filter(user=request.user).filter(edition=edition)
    return render(request, 'buecher/books/edition/edition.html', locals())
