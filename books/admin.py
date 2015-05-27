from django.contrib import admin

from books.models import Book, BookRating

admin.site.register(Book)
admin.site.register(BookRating)
