from django.urls import path
from .views import (
    BooksList, BookDetails,
    BookCreateView, BookUpdateView
)

urlpatterns = [
    path('', BooksList.as_view(), name='book_list'),
    path('<int:pk>/', BookDetails.as_view(), name='book_detail'),
    path('new/', BookCreateView.as_view(), name='book_create'),
    path('<int:pk>/edit/', BookUpdateView.as_view(), name='book_edit'),
]
