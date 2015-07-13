from django.shortcuts import get_object_or_404, render
from persons.models import Person

def person(request, slug):
    person = get_object_or_404(Person, slug=slug)
    return render(request, 'buecher/persons/person/person.html', locals())
