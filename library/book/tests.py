from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve

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
