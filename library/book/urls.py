from django.urls import path
from .views import BookListView, BookDetailView
from . import views


urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('add/', views.book_form, name='book_form'),
    path('<int:pk>/', BookDetailView.as_view(), name='book_update'),
    path('delete/<int:pk>/', views.book_delete, name='book_delete'),
]