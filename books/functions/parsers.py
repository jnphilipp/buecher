from datetime import date, datetime
import bibtexparser
import re


def bibtex(text):
	bib_database = bibtexparser.loads(text)
	entries = []
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
		publisher = entry['publisher'] if 'publisher' in entry else ''
		year = date(year=int(entry['year']), month=1, day=1) if 'year' in entry else None
		published_on = datetime.strptime(entry['timestamp'], '%a, %d %b %Y %H:%M:%S %z').date() if 'timestamp' in entry else year
		url = entry['link'] if 'link' in entry else ''

		entries.append({'title':title, 'authors':authors, 'journal':journal, 'volume':volume, 'publisher':publisher, 'published_on':published_on, 'url':url})
	return entries