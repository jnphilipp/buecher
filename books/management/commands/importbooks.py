from books.models import Book
from django.core.management.base import BaseCommand
from os.path import exists
from persons.models import Person
from series.models import Series

class Command(BaseCommand):
    help = 'Import books from csv.'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        path = options['csv_file'].strip()
        if not exists(path):
            self.stdout.write('CSV file not found. Abborting...')
            return

        with open(path, 'r') as f:
            for line in f:
                fields = line.strip().split(',')
                book, created = Book.objects.get_or_create(title=fields[0])
                series, created = Series.objects.get_or_create(name=fields[1])
                book.series = series
                book.volume = float(fields[2])
                book.save()
                for i in range(3, len(fields)):
                    lastname, firstname = fields[i].split(';')
                    person, created = Person.objects.get_or_create(first_name=firstname, last_name=lastname)
                    book.authors.add(person)
                book.save()
        f.close()
        self.stdout.write('Successfully imported books.')
