from django.views.generic import ListView, View
from django.shortcuts import redirect, get_object_or_404, render
from .models import Author
from book.models import Book

class AuthorList(ListView):
    model = Author
    template_name = 'author/authors_list.html'
    context_object_name = 'authors'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        name_query = self.request.GET.get('name')
        surname_query = self.request.GET.get('surname')

        if name_query:
            queryset = queryset.filter(name__icontains=name_query)

        if surname_query:
            queryset = queryset.filter(surname__icontains=surname_query).distinct()

        return queryset


class AuthorDelete(View):
    def post(self, request, author_id):
        author = get_object_or_404(Author, id=author_id)

        if not author.books.exists():
            author.delete()

        return redirect('authors-list')

class AuthorCreate(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'author/author_create.html', {'books': books})

    def post(self, request):
        name = request.POST.get('name', '').strip()
        surname = request.POST.get('surname', '').strip()
        patronymic = request.POST.get('patronymic', '').strip()
        selected_books = request.POST.getlist('books')

        if not (name and surname and patronymic):
            return redirect('authors-list')

        if len(name) > 20 or len(surname) > 20 or len(patronymic) > 20:
            return redirect('authors-list')

        author = Author.objects.create(name=name, surname=surname, patronymic=patronymic)
        author.books.set(selected_books)
        author.save()
        return redirect('authors-list')