from django.conf import settings
from django.db import models
import os
import shutil

def get_ebook_path(instance, filename):
	name = instance.book.title if not instance.book.authors else u"%s - %s" % (instance.book.title, u", ".join([unicode(author) for author in instance.book.authors.all()]))
	return os.path.join('books', unicode(instance.book.id), name + os.path.splitext(filename)[1])

class Person(models.Model):
	firstname = models.TextField()
	lastname = models.TextField()

	def __unicode__(self):
		return u"%s %s" % (self.firstname, self.lastname)

	class Meta:
		ordering = ('lastname', 'firstname')

class Publisher(models.Model):
	name = models.TextField()

	def __unicode__(self):
		return self.name

class Binding(models.Model):
	binding = models.TextField()

	def __unicode__(self):
		return self.binding

class Language(models.Model):
	language = models.TextField()

	def __unicode__(self):
		return self.language

	class Meta:
		ordering = ('language',)

class Series(models.Model):
	name = models.TextField()

	def __unicode__(self):
		return self.name

class Book(models.Model):
	updated_at = models.DateTimeField(auto_now=True)
	created_at = models.DateTimeField(auto_now_add=True)

	title = models.TextField()
	isbn = models.CharField(max_length=13, blank=True)
	asin = models.CharField(max_length=10, blank=True)
	price = models.FloatField(default=0)
	published_on = models.DateField()
	purchased_on = models.DateField(blank=True, null=True)
	read_on = models.DateField(blank=True, null=True)

	cover_image = models.ImageField(upload_to='books', blank=True, null=True)

	binding = models.ForeignKey(Binding, blank=True, null=True)
	languages = models.ManyToManyField(Language, blank=True, null=True)
	authors = models.ManyToManyField(Person, blank=True, null=True)
	publisher = models.ForeignKey(Publisher, blank=True, null=True)

	series = models.ForeignKey(Series, blank=True, null=True)
	volume = models.FloatField(blank=True, null=True)

	def save(self):
		if self.id is None:
			super(Book, self).save()
			if self.cover_image.name:
				self.cover_image = self.get_image_path(self.cover_image)
				super(Book, self).save()
		else:
			super(Book, self).save()
			if self.cover_image.name:
				self.cover_image = self.get_image_path(self.cover_image)
				super(Book, self).save()

	def get_image_path(self, filename):
		save_name = os.path.join('books', unicode(self.id), 'cover.jpg')
		current_path = os.path.join(settings.MEDIA_ROOT, self.cover_image.path)
		new_path = os.path.join(settings.MEDIA_ROOT, save_name)

		if os.path.exists(current_path):
			if not os.path.exists(os.path.dirname(new_path)):
				os.makedirs(os.path.dirname(new_path))

			shutil.move(current_path, new_path)

		return save_name

	def get_absolute_url(self):
		return "/books/%i/" % self.id

	def get_authors(self):
		return u", ".join([unicode(author) for author in self.authors.all()])

	def __unicode__(self):
		base = self.title if not self.authors else u"%s - %s" % (self.title, u", ".join([unicode(author) for author in self.authors.all()]))
		base = base if not self.series else u"%s (%s #%s)" % (base, unicode(self.series), unicode(self.volume))
		return base

class EBookFile(models.Model):
	ebook_file = models.FileField(upload_to=get_ebook_path)
	book = models.ForeignKey(Book)

	def __unicode__(self):
		return self.ebook_file.url