from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Author
from .forms import AuthorForm
from django.db.models import Q


class AuthorListView(ListView):
    context_object_name = 'authors'
    model = Author

def author_form(request, pk=None):
    if request.method == 'GET':
        if pk == None:
            form = AuthorForm()
        else:
            author = Author.objects.get(id=pk)
            form = AuthorForm(instance=author)
        return render(request, 'author/author_form.html', {'form': form})
    else:
        if pk == None:
            form = AuthorForm(request.POST)
        else:
            author = Author.objects.get(id=pk)
            form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
        return redirect('/author/')

def author_delete(request, pk):
    author = Author.objects.get(id=pk)
    author.delete()
    return redirect('/author/')