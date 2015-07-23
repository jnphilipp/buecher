from buechers.models import List
from buechers.templatetags.buecher import register
from django.utils import timezone

@register.filter
def floatdot(value, precision=2):
    return round(value, precision)

@register.filter
def decrement(value):
    return int(value) - 1

@register.filter
def increment(value):
    return int(value) + 1

@register.filter
def lookup(d, key):
    return d[key] if key in d else None

@register.filter
def startswith(value, start):
    return value.startswith(start)

@register.filter
def previous(value, arg):
    try:
        return value[int(arg) - 1] if int(arg) - 1 != -1 else None
    except:
        return None

@register.filter
def next(value, arg):
    try:
        return value[int(arg) + 1]
    except:
        return None

@register.filter(name='addcss')
def addcss(field, css):
    return field.as_widget(attrs={"class":css})

@register.simple_tag
def edition_read(read):
    if read.started and read.finished:
        return '%s days, %s - %s' % ((read.finished - read.started).days, read.started.strftime('%d. %B %Y'), read.finished.strftime('%d. %B %Y'))
    elif read.started:
        return '%s days, started on %s' % ((timezone.now().date() - read.started).days, read.started.strftime('%d. %B %Y'))
    elif read.finished:
        return 'finished on %s' % read.finished.strftime('%d. %B %Y')
    else:
        return ''

@register.assignment_tag
def user_lists(user):
    if user.is_authenticated():
        return List.objects.filter(user=user)
    else:
        return None
