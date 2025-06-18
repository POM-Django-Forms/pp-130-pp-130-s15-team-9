from django.contrib import admin
from .models import Author

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

if admin.site.is_registered(Author):
    admin.site.unregister(Author)

admin.site.register(Author, AuthorAdmin)
