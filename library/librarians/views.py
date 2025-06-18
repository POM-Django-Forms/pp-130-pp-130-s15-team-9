from django.shortcuts import render, get_object_or_404
from .models import Librarian

def список_бібліотекарів(request):
    бібліотекарі = Librarian.objects.all()
    return render(request, 'librarians/список_бібліотекарів.html', {'бібліотекарі': бібліотекарі})

def деталі_бібліотекаря(request, pk):
    бібліотекар = get_object_or_404(Librarian, pk=pk)
    return render(request, 'librarians/деталі_бібліотекаря.html', {'бібліотекар': бібліотекар})
