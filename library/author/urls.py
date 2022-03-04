from django.urls import path
from .views import AuthorListView
from . import views


urlpatterns = [
    path('', AuthorListView.as_view(), name='author_list'),
    path('add/', views.author_form, name='author_form'),
    path('<int:pk>/', views.author_form, name='author_update'),
    path('delete/<int:pk>/', views.author_delete, name='author_delete'),
    #path('<int:pk>/books/', views.author_books, name='author_books'),
]