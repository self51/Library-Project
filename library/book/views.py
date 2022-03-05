from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Book, Author
from .forms import BookForm
from django.db.models import Q


class BookListView(ListView):
    context_object_name = 'books'
    model = Book

class BookDetailView(DetailView):
    queryset = Book.objects.all()
    context_object_name = 'book'

def book_form(request, pk=None):
    if request.method == 'GET':
        if pk == None:
            form = BookForm()
        else:
            book = Book.objects.get(pk)
            form = BookForm(instance=book)
        return render(request, 'book/book_form.html', {'form': form})
    else:
        if pk == None:
            form = BookForm(request.POST)
        else:
            book = Book.objects.get(pk)
            form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
        return redirect('/book/')


def book_delete(request, pk):
    pass