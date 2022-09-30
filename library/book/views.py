from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.db.models import Q

from .models import Book, Author
from .forms import BookForm


class BookListView(ListView):
    context_object_name = 'books'
    model = Book

    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get('q')
        sort_option = self.request.GET.get('sort_by')

        if query:
            return Book.objects.filter(Q(name__icontains=query)|
                                      Q(author__name__icontains=query)|
                                      Q(author__surname__icontains=query)).distinct()

        elif sort_option:
            if sort_option == 'name(descending)':
                return Book.objects.order_by('-name')
            if sort_option == 'name(ascending)':
                return Book.objects.order_by('name')
            if sort_option == 'count(ascending)':
                return Book.objects.order_by('count')
            if sort_option == 'count(descending)':
                return Book.objects.order_by('-count')

        return Book.objects.order_by('name').prefetch_related('author')


class BookDetailView(DetailView):
    queryset = Book.objects.all()
    context_object_name = 'book'


def book_form(request, pk=None):
    if request.method == 'GET':
        if pk == None:
            form = BookForm()
        else:
            book = Book.objects.get(id=pk)
            form = BookForm(instance=book)
        return render(request, 'book/book_form.html', {'form': form})
    else:
        if pk == None:
            form = BookForm(request.POST)
        else:
            book = Book.objects.get(id=pk)
            form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
        return redirect('/book/')


def book_delete(request, pk):
    book = Book.objects.get(id=pk)
    book.delete()
    return redirect('/book/')