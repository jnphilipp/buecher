from books.functions.date import next
from books.models import Binding, Book, EBookFile, Language, Series, Url
from datetime import date
from django.conf import settings
from django.core import management
from django.core.mail import mail_admins
from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError
from django.db.models import Max
from django.template.defaultfilters import slugify
from http import client as HTTP
from os import makedirs
from os.path import exists, join
from urllib.error import HTTPError
from urllib.request import urlopen, urlretrieve

class Command(BaseCommand):
	help = 'Checks the status of the freiesMagazin (http://www.freiesmagazin.de) issues in the database against the online status and adds the new issues.'

	def handle(self, *args, **options):
		series, created = Series.objects.get_or_create(name='freiesMagazin')
		binding, created = Binding.objects.get_or_create(name='E-Book')
		language, created = Language.objects.get_or_create(name='Deutsch')
		volume = Book.objects.filter(series=series).aggregate(Max('volume'))['volume__max']
		if volume == None:
			volume = 0
			month = (2006, 2)
		else:
			title = Book.objects.get(series=series, volume=volume).title
			month = (int(title[-4:]), int(title[-7:]-5))

		code = HTTP.OK
		while code == HTTP.OK:
			volume += 1
			month = next(month)
			try:
				code = urlopen('http://www.freiesmagazin.de/freiesMagazin-%d-%02d' % (month[0], month[1])).code
				if code == HTTP.OK:
					self.stdout.write('Adding Issue %d (%02d/%d)...' % (volume, month[1], month[0]))
					book = Book(title='freiesMagazin %02d/%d' % (month[1], month[0]), series=series, volume=volume, binding=binding, published_on=date(year=month[0], month=month[1], day=1), purchased_on=date.today())
					book.save()
					book.languages.add(language)
					book.save()

					folder = join(settings.MEDIA_ROOT, 'books', str(book.id))
					if not exists(folder):
						makedirs(folder)

					image = join(folder, 'cover.jpg')
					try:
						urlretrieve('http://www.freiesmagazin.de/system/files/freiesmagazin-%d-%02d.png' % (month[0], month[1]), image)
						book.cover_image = image
						book.save()
					except HTTPError as e:
						pass

					name = slugify('freiesMagazin-%d-%02d' % (month[0], month[1])) + '.pdf'
					pdf = join(folder, name)
					urlretrieve('http://www.freiesmagazin.de/ftp/%d/freiesMagazin-%d-%02d.pdf' % (month[0], month[0], month[1]), pdf)
					EBookFile.objects.create(ebook_file=join('books', str(book.id), name), book=book)

					try:
						name = slugify('freiesMagazin-%d-%02d' % (month[0], month[1])) + '.epub'
						epub = join(folder, name)
						urlretrieve('http://www.freiesmagazin.de/ftp/%d/freiesMagazin-%d-%02d-bilder.epub' % (month[0], month[0], month[1]), epub)
						EBookFile.objects.create(ebook_file=join('books', str(book.id), name), book=book)
					except HTTPError as e:
						pass

					Url.objects.create(url='http://www.freiesmagazin.de/freiesMagazin-%d-%02d' % (month[0], month[1]), book=book)
					book.save()
			except HTTPError as e:
				self.stdout.write('No Issue %d (%02d/%d), stopping.' % (volume, month[1], month[0]))
				break