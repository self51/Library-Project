from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve

from author.views import AuthorListView, author_form, author_delete, author_books


class TestUrl(SimpleTestCase):

    def test_author_list_resolves(self):
        url = reverse('author_list')
        self.assertEqual(resolve(url).func.view_class, AuthorListView)

    def test_add_author_url_resolves(self):
        url = reverse('author_form')
        self.assertEqual(resolve(url).func, author_form)

    def test_author_update_url_resolves(self):
        url = reverse('author_update', args=[1])
        self.assertEqual(resolve(url).func, author_form)

    def test_author_delete_url_resolves(self):
        url = reverse('author_delete', args=[1])
        self.assertEqual(resolve(url).func, author_delete)

    def test_author_books_url_resolves(self):
        url = reverse('author_books', args=[1])
        self.assertEqual(resolve(url).func, author_books)

