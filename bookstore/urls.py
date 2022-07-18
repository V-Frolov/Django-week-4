from django.urls import path
from bookstore.views import *

urlpatterns = [
    path('', BooksView.as_view(), name='list_books'),                   # List of all books
    path('book/<int:index>', current_book, name='current_book'),        # Show current book
    path('author/<int:index_author>/', about_author, name='author'),    # Show info about author
    path('create_book/', create_book, name='create_book'),              # Create new great book
    path('delete_book/<int:index>/', delete_book, name='delete_book'),  # Delete this great book
    path('author_book/<int:index_author>/author_book', author_book, name='author_book'),
]                                                                       # Show info about all books of this author
