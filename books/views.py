from books.models import Book
from books.models import EBookFile
from django.shortcuts import get_object_or_404, get_list_or_404, render_to_response

def index(request):
	books = Book.objects.all().order_by('-updated_at')
	return render_to_response('books/index.html', {'books': books})

def detail(request, book_id):
	book = get_object_or_404(Book, pk=book_id)
	ebook_files = EBookFile.objects.filter(book=book_id)
	return render_to_response('books/detail.html', {'book': book, 'ebook_files': ebook_files})