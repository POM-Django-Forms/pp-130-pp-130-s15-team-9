from django.urls import path
from .views import BooksList, BookDetails

urlpatterns = [
    path('', BooksList.as_view(), name='books_list'),
    path('<int:pk>/', BookDetails.as_view(), name='book_detail')
]
