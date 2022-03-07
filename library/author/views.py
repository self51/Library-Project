from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Author
from .forms import AuthorForm
from django.db.models import Q


class AuthorListView(ListView):
    context_object_name = 'authors'
    model = Author

    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get('q')
        sort_option = self.request.GET.get('sort_by')

        if query:
            return Author.objects.filter(Q(name__icontains=query)|
                                      Q(surname__icontains=query)|
                                      Q(patronymic__icontains=query)).distinct()

        elif sort_option:
            if sort_option == 'name(descending)':
                return Author.objects.order_by('-name')
            if sort_option == 'name(ascending)':
                return Author.objects.order_by('name')
            if sort_option == 'surname(ascending)':
                return Author.objects.order_by('surname')
            if sort_option == 'surname(descending)':
                return Author.objects.order_by('-surname')

        return Author.objects.order_by('name')

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