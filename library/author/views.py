from django.views.generic import ListView, View
from django.shortcuts import render, redirect, get_object_or_404

from .models import Author
from .forms import AuthorForm

class AuthorList(ListView):
    model = Author
    template_name = 'author/author_list.html'
    context_object_name = 'authors'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        name_q = self.request.GET.get('name')
        surname_q = self.request.GET.get('surname')

        if name_q:
            qs = qs.filter(name__icontains=name_q)
        if surname_q:
            qs = qs.filter(surname__icontains=surname_q)

        return qs

class AuthorCreate(View):
    def get(self, request):
        form = AuthorForm()
        return render(request, 'author/author_create.html', {
            'form': form
        })

    def post(self, request):
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authors-list')
        # Якщо форма не валідна — повертаємо її з помилками
        return render(request, 'author/author_create.html', {
            'form': form
        })

class AuthorDelete(View):
    def post(self, request, author_id):
        author = get_object_or_404(Author, id=author_id)
        # Видаляємо лише якщо в автора немає книжок
        if not author.books.exists():
            author.delete()
        return redirect('authors-list')