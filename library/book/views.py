from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Book
from django.utils import timezone
from datetime import timedelta
import pytz

class BooksList(ListView):
    model = Book
    template_name = 'book/books_list.html'
    context_object_name = 'books'
    paginate_by = 4

    def get_queryset(self):
        queryset = super().get_queryset()
        name_query = self.request.GET.get('name')
        author_query = self.request.GET.get('author')

        if name_query:
            queryset = queryset.filter(name__icontains=name_query)

        if author_query:
            queryset = queryset.filter(authors__surname__icontains=author_query).distinct()

        return queryset


class BookDetails(DetailView):
    model = Book
    template_name = "book/book_detail.html"
    context_object_name = "book"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kyiv_tz = pytz.timezone('Europe/Kyiv')

        now = timezone.now().astimezone(kyiv_tz)
        two_months_later = now + timedelta(days=60)

        context.update(
            {
            'min_date': now.strftime('%Y-%m-%dT%H:%M'),
            'max_date': two_months_later.strftime('%Y-%m-%dT%H:%M')}
        )

        return context
