from django.urls import path
from .views import home_view, login_view, register_view, logout_view
from .views import edit_profile_view
urlpatterns = [
    path('', home_view, name='home'),
    path('edit/', edit_profile_view, name='edit_profile'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
]
