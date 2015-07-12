from books.templatetags.books import register
from django.templatetags.static import static

@register.filter
def shorttitle(book, length):
    author = book.authors.first()
    if author:
        if book.series:
            if (len(str(author)) + len(book.title) + len(str(book.series)) + len('%g' % book.volume) + 11) > length:
                length -= (len(str(author)) + len('%g' % book.volume) + 11)
                return '%s… by %s (%s… #%g)' % (book.title[:int(length / 2)], author, str(book.series)[:int(length / 2)], book.volume)
            else:
                return '%s by %s (%s #%g)' % (book.title, author, book.series, book.volume)
        else:
            if (len(str(author)) + len(book.title) + 5) > length:
                return '%s… by %s' % (book.title[:(length - 5 - len(str(author)))], author)
            else:
                return '%s by %s' % (book.title, author)
    else:
        return book.title[:length]

@register.filter
def image(book):
    if book.editions.first() and book.editions.first().cover_image:
        return book.editions.first().cover_image.url
    else:
        return static('images/default_cover.jpg')
