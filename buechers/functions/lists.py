from buechers.models import List

def update_possesion_list(possesion, user, edition):
    try:
        wishlist = List.objects.get(user=user, name='wishlist', editions=edition)
        wishlist.editions.remove(edition)
        wishlist.save()
    except List.DoesNotExist:
        pass
    try:
        wishlist = List.objects.get(user=user, name='wishlist', books=edition.book)
        wishlist.books.remove(edition.book)
        wishlist.save()
    except List.DoesNotExist:
        pass
    try:
        unread = List.objects.get(user=user, name='unread books')
        unread.editions.add(edition)
        unread.save()
    except List.DoesNotExist:
        pass

def update_read_list(read, user, edition):
    if read.started and not read.finished:
        try:
            unread = List.objects.get(user=request.user, name='unread books', editions=edition)
            unread.editions.remove(edition)
            unread.save()
        except List.DoesNotExist:
            pass
        try:
            unread = List.objects.get(user=request.user, name='unread books', books=edition.book)
            unread.books.remove(edition.book)
            unread.save()
        except List.DoesNotExist:
            pass
        try:
            reading = List.objects.get(user=request.user, name='reading books')
            reading.editions.add(edition)
            reading.save()
        except List.DoesNotExist:
            pass
    elif read.finished:
        try:
            reading = List.objects.get(user=request.user, name='reading books', editions=edition)
            reading.editions.remove(edition)
            reading.save()
        except List.DoesNotExist:
            pass
        try:
            reading = List.objects.get(user=request.user, name='reading books', books=edition.book)
            reading.books.remove(edition.book)
            reading.save()
        except List.DoesNotExist:
            pass
        try:
            read = List.objects.get(user=request.user, name='read books')
            read.editions.add(edition)
            read.save()
        except List.DoesNotExist:
            pass
