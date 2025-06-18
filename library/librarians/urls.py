from django.urls import path
from librarians.migrations import views

urlpatterns = [
    path('бібліотекарі/', views.список_бібліотекарів, name='список_бібліотекарів'),
    path('бібліотекарі/<int:pk>/', views.деталі_бібліотекаря, name='деталі_бібліотекаря'),
]
