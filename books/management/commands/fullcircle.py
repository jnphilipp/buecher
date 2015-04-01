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
	help = 'Checks the status of the Full Circle Magazine (http://fullcirclemagazine.org) issues in the database against the online status and adds the new issues.'

	def handle(self, *args, **options):
		series, created = Series.objects.get_or_create(name='Full Circle Magazine')
		binding, created = Binding.objects.get_or_create(name='E-Book')
		language, created = Language.objects.get_or_create(name='Englisch')
		volume = Book.objects.filter(series=series).aggregate(Max('volume'))['volume__max']
		if volume == None:
			volume = 0

		code = HTTP.OK
		while code == HTTP.OK:
			volume += 1
			try:
				code = urlopen('http://fullcirclemagazine.org/issue-%d/' % volume).code
				if code == HTTP.OK:
					self.stdout.write('Adding Issue %d...' % volume)
					book = Book(title='Issue %d' % volume, series=series, volume=volume, binding=binding, purchased_on=date.today())
					book.save()
					book.languages.add(language)
					book.save()

					folder = join(settings.MEDIA_ROOT, 'books', str(book.id))
					if not exists(folder):
						makedirs(folder)

					image = join(folder, 'cover.jpg')
					urlretrieve('http://dl.fullcirclemagazine.org/cover/%d/xen.jpg.pagespeed.ic.OYt0Nw3Yh8.jpg' % volume, image)
					book.cover_image = image
					book.save()

					name = slugify('Issue %d' % volume) + '.pdf'
					pdf = join(folder, name)
					urlretrieve('http://dl.fullcirclemagazine.org/issue%d_en.pdf' % volume, pdf)
					EBookFile.objects.create(ebook_file=join('books', str(book.id), name), book=book)

					name = slugify('Issue %d' % volume) + '.epub'
					epub = join(folder, name)
					urlretrieve('http://dl.fullcirclemagazine.org/issue%d_en.epub' % volume, epub)
					EBookFile.objects.create(ebook_file=join('books', str(book.id), name), book=book)

					Url.objects.create(url='http://fullcirclemagazine.org/issue-%d/' % volume, book=book)
					book.save()
			except HTTPError as e:
				self.stdout.write('No Issue %d, stopping.' % volume)
				break