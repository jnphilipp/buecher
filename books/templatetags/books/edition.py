from books.templatetags.books import register
from buechers.models import Possession, Read

@register.filter
def possessions(edition, user):
    return Possession.objects.filter(user=user).filter(edition=edition) if not user.is_anonymous() else None

@register.filter
def reads(edition, user):
    return Read.objects.filter(user=user).filter(edition=edition) if not user.is_anonymous() else None
