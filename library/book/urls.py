from django.views.decorators.cache import cache_page
from django.urls import path
from .views import BookListView, BookDetailView
from . import views


urlpatterns = [
    path('', cache_page(60)(BookListView.as_view()), name='book_list'),
    path('add/', views.book_form, name='book_form'),
    path('<int:pk>/', cache_page(60)(BookDetailView.as_view()), name='book_detail'),
    path('update/<int:pk>/', views.book_form, name='book_update'),
    path('delete/<int:pk>/', views.book_delete, name='book_delete'),
]