from django.shortcuts import get_object_or_404, render
from series.models import Series

def series(request, slug):
    series = get_object_or_404(Series, slug=slug)
    return render(request, 'buecher/series/series/series.html', locals())
