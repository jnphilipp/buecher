from books.models import Edition
from django.shortcuts import get_object_or_404, render

def edition(request, slug, edition_id):
    edition = get_object_or_404(Edition, book__slug=slug, id=edition_id)
    return render(request, 'buecher/books/edition/edition.html', locals())
