from django.urls import path
from .views import AuthorList, AuthorDelete, AuthorCreate

urlpatterns = [
    path('authors/', AuthorList.as_view(), name='authors-list'),
    path('authors/delete/<int:author_id>/', AuthorDelete.as_view(), name='remove-author'),
    path('authors/create/', AuthorCreate.as_view(), name='author-create'),
]
