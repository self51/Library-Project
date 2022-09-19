from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve

from author.models import Author
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


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.author_list_url = reverse('author_list')
        self.author_books_url = reverse('author_books', args=[1])
        self.author_add_url = reverse('author_form')
        self.author = Author.objects.create(
            name="Person",
            surname="Person_surname",
            patronymic="Person_patronymic",
        )

    def test_author_list_view(self):
        response = self.client.get(self.author_list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'author/author_list.html')

    def test_author_books(self):
        response = self.client.get(self.author_books_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book/book_list.html')

    def test_author_form_get(self):
        response_add = self.client.get(self.author_add_url)
        response_update = self.client.get(reverse('author_update', args=[3]))

        self.assertEqual(response_add.status_code, 200)
        self.assertTemplateUsed(response_add, 'author/author_form.html')
        self.assertEqual(response_update.status_code, 200)
        self.assertTemplateUsed(response_update, 'author/author_form.html')

    def test_author_form_post(self):
        response_add = self.client.post(self.author_add_url, {
            'name': 'Person1',
            'surname': "Person_surname",
            'patronymic': "Person_patronymic"
        })


        self.assertEqual(response_add.status_code, 302)
        self.assertEqual(Author.objects.get(id=5).name, 'Person1')

        response_update = self.client.post(reverse('author_update', args=[4]), {
            'name': 'name1',
            'surname': "Person_surname",
            'patronymic': "Person_patronymic"
        })

        self.assertEqual(response_update.status_code, 302)
        self.assertEqual(Author.objects.get(id=4).name, 'name1')


    def test_author_delete(self):
        response = self.client.delete(reverse('author_delete', args=[2]))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Author.objects.all().count(), 0)

