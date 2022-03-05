from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'description', 'count', 'author')
        labels = {
            'name': 'Name',
            'count': 'Count',
        }

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['author'].empty_label = 'Select'
        self.fields['author'].require = False
        self.fields['description'].require = False