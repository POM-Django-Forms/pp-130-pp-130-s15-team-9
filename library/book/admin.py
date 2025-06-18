from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'author', 'year_published', 'date_issued')

if admin.site.is_registered(Book):
    admin.site.unregister(Book)

admin.site.register(Book, BookAdmin)
