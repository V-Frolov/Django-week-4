from django.shortcuts import render, redirect, get_object_or_404
from bookstore.models import Books, Authors
from bookstore.forms import CreateBook
from django.views.generic.base import View
from django.views.generic.detail import DetailView


class BooksView(View):                              # List of all books
    def post(self, request):
        form = CreateBook(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            title = data['title']
            released_year = data['released_year']
            description = data['description']
            author_id = data['author_id']
            Books.objects.create(title=title, released_year=released_year, description=description, author_id=author_id)
            book = Books.objects.all()
        context = {'books': book, 'book_form': CreateBook}
        return render(request, 'bookstore/List_books.html', context=context)

    def get(self, request):
        book = Books.objects.all()
        if "search" in request.GET:
            book_search = request.GET['search']
            book = book.filter(title__contains=book_search)
        context = {'books': book, 'book_form': CreateBook}
        return render(request, 'bookstore/List_books.html', context=context)


class BookDetailView(DetailView):                   # ???
    model = Books
    template_name = 'bookstore/Current_book.html'


def current_book(request, index):                   # Show current book
    try:
        book = Books.objects.get(pk=index)
        return render(request, 'bookstore/Current_book.html', context={'books': book})
    except:
        return render(request, 'bookstore/Page404.html')


def about_author(request, index_author):            # Show info about author
    try:
        author = Authors.objects.get(pk=index_author)
        return render(request, 'bookstore/About_author.html', context={'author': author})
    except:
        return render(request, 'bookstore/Page404.html')


def author_book(request, index_author):             # Show info about all books of this author
    try:
        author = Authors.objects.get(pk=index_author)
        author = str(author.first_name) + ' ' + str(author.last_name)
        author_book = list(filter(lambda book: book['author_id'] == index_author, Books.objects.values()))
        return render(request, 'bookstore/Author_book.html', context={'author_book': author_book, 'author': author})
    except:
        return render(request, 'bookstore/Page404.html')


def create_book(request):                           # Create new great book
    book = Books.objects.all()
    if "search" in request.GET:
        book_search = request.GET['search']
        book = book.filter(title__contains=book_search)
    if request.method == "POST":
        form = CreateBook(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            title = data['title']
            released_year = data['released_year']
            description = data['description']
            author_id = data['author_id']
            Books.objects.create(title=title, released_year=released_year, description=description, author_id=author_id)
            book = Books.objects.all()
            context = {'books': book, 'book_form': CreateBook}
            return redirect('list_books')
        else:
            form = CreateBook()
    context = {'books': book, 'book_form': CreateBook}
    return render(request, 'bookstore/Create_book.html', context=context)


def delete_book(request, index):                    # Delete this great book
    book = get_object_or_404(Books, id=index)
    book.delete()
    return redirect('list_books')
