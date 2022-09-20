from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve

from author.models import Author
from book.models import Book
from book.views import BookListView, BookDetailView, book_form, book_delete


class TestUrl(SimpleTestCase):

    def test_book_list_resolves(self):
        url = reverse('book_list')
        self.assertEqual(resolve(url).func.view_class, BookListView)

    def test_book_detail_url_resolves(self):
        url = reverse('book_detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, BookDetailView)

    def test_add_book_url_resolves(self):
        url = reverse('book_form')
        self.assertEqual(resolve(url).func, book_form)

    def test_book_update_url_resolves(self):
        url = reverse('book_update', args=[1])
        self.assertEqual(resolve(url).func, book_form)

    def test_book_delete_url_resolves(self):
        url = reverse('book_delete', args=[1])
        self.assertEqual(resolve(url).func, book_delete)


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.book_list_url = reverse('book_list')
        self.books_detail_url = reverse('book_detail', args=[2])
        self.author = Author.objects.create(
            name="Person",
            surname="Person_surname",
            patronymic="Person_patronymic",
        )
        self.book = Book.objects.create(
            name="Simple book",
        )
        self.book.author.add(self.author)

    def test_book_list_view(self):
        response = self.client.get(self.book_list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book/book_list.html')

    def test_book_detail_view(self):
        response = self.client.get(self.books_detail_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book/book_detail.html')

    def test_book_form_get(self):
        response_add = self.client.get(reverse('book_form'))
        response_update = self.client.get(reverse('book_update', args=[3]))

        self.assertEqual(response_add.status_code, 200)
        self.assertTemplateUsed(response_add, 'book/book_form.html')
        self.assertEqual(response_update.status_code, 200)
        self.assertTemplateUsed(response_update, 'book/book_form.html')

    def test_book_form_post(self):
        response_add = self.client.post(reverse('book_form'), {
            'name': 'New_book',
            'count': 10,
            'author': [4,]
        })

        self.assertEqual(response_add.status_code, 302)
        self.assertEqual(Book.objects.get(id=5).name, 'New_book')

        response_update = self.client.post(reverse('book_update', args=[5]), {
            'name': 'Book_updated',
            'count': 10,
            'author': [4, ]
        })

        self.assertEqual(response_update.status_code, 302)
        self.assertEqual(Book.objects.get(id=5).name, 'Book_updated')

    def test_book_delete(self):
        response = self.client.delete(reverse('book_delete', args=[1]))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Book.objects.all().count(), 0)

