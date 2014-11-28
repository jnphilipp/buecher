from books.models import Binding, Book, EBookFile, Language, Series, Url
from datetime import date, datetime
from django.conf import settings
from django.core import management
from django.core.mail import mail_admins
from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError
from django.db.models import Max
from http import client as HTTP
from os import makedirs
from os.path import exists, join
from urllib.error import HTTPError
from urllib.request import urlopen, urlretrieve

import bibtexparser
import re

class Command(BaseCommand):
	help = 'Parses the given bibtex file and adds the book.'

	def handle(self, *args, **options):
		if len(args) != 1:
			self.stdout.write('fromBibTex <bibtex file>')
			return

		with open(args[0]) as bibtex_file:
			bibtex_str = bibtex_file.read()

		bib_database = bibtexparser.loads(bibtex_str)
		for entry in bib_database.entries:
			title = entry['title'] if 'title' in entry else ''
			authors = []
			for author in re.compile(r'\s*and\s*').split(re.sub(r'(?s)\s*\n\s*', ' ', entry['author'])):
				if ',' in author:
					s = author.split(',')
					authors.append({'firstname':s[1], 'lastname':s[0]})
				else:
					s = author.rsplit(' ', 1)
					authors.append({'firstname':s[0], 'lastname':s[1]})

			journal = entry['journal'] if 'journal' in entry else ''
			volume = entry['volume'] if 'volume' in entry else ''
			volume = '%s.%s' % (volume, entry['number']) if 'number' in entry else volume
			publisher = entry['publisher'] if 'publisher' in entry else None

			year = date(year=int(entry['year']), month=1, day=1) if 'year' in entry else None
			published_on = datetime.strptime(entry['timestamp'], '%a, %d %b %Y %H:%M:%S %z').date() if 'timestamp' in entry else year
			url = entry['link'] if 'link' in entry else ''

			self.stdout.write('title: %s' % title)
			self.stdout.write('authors: %s' % ', '.join(str(author) for author in authors))
			self.stdout.write('journal: %s' % journal)
			self.stdout.write('volume: %s' % volume)
			self.stdout.write('publisher: %s' % publisher)
			self.stdout.write('published on: %s' % published_on)
			self.stdout.write('url: %s' % url)

			print('##################################################')