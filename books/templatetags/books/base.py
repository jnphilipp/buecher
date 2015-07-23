from books.models import Book, Edition
from books.templatetags.books import register
from django.templatetags.static import static

@register.filter
def shorttitle(book, length):
    return book.shorttitle(length)

@register.filter
def image(book):
    if book.editions.first() and book.editions.first().cover_image:
        return book.editions.first().cover_image.url
    else:
        return static('images/default_cover.jpg')
