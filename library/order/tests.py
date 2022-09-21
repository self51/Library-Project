from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve

from django.contrib.auth.models import User
from author.models import Author
from book.models import Book
from order.models import Order
from order.views import OrderListView, user_orders, order_form, order_delete


class TestUrl(SimpleTestCase):

    def test_order_list_url_resolves(self):
        url = reverse('order_list')
        self.assertEqual(resolve(url).func.view_class, OrderListView)

    def test_user_orders_url_resolves(self):
        url = reverse('user_orders', args=[1])
        self.assertEqual(resolve(url).func, user_orders)

    def test_order_form_url_resolves(self):
        url = reverse('order_form' , args=[1])
        self.assertEqual(resolve(url).func, order_form)

    def test_order_delete_url_resolves(self):
        url = reverse('order_delete' , args=[1])
        self.assertEqual(resolve(url).func, order_delete)


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.order_list_url = reverse('order_list')
        self.user_orders_url = reverse('user_orders', args=[5])
        self.order_add_url = reverse('order_form', args=[2])
        self.delete_order_url = reverse('order_delete', args=[1])
        self.user = User.objects.create_user(
            username = 'simple_user',
            password = 'password12Q',
        )
        self.author = Author.objects.create(
            name="Person",
            surname="Person_surname",
            patronymic="Person_patronymic",
        )
        self.book = Book.objects.create(
            name="Simple book",
            count="1"
        )
        self.book.author.add(self.author)

    def test_order_list_view(self):
        response = self.client.get(self.order_list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'order/order_list.html')

    def test_user_orders(self):
        response = self.client.get(self.user_orders_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'order/user_orders.html')

    def test_order_form(self):
        self.client.login(username='simple_user', password='password12Q')
        response = self.client.post(self.order_add_url)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Order.objects.get(id=2).book.name, 'Simple book')
        self.assertEqual(Book.objects.get(id=2).count, 0)

    def test_order_form_if_book_count_is_zero(self):
        zero_books = Book.objects.create(
            name="Zero books",
            count=0,
        )
        self.client.login(username='simple_user', password='password12Q')
        response = self.client.post(reverse('order_form', args=[4]), follow=True)
        message = list(response.context.get('messages'))[0]

        self.assertEqual(Book.objects.get(id=4).count, 0)
        self.assertEqual(Order.objects.all().count(), 0)
        self.assertEqual(str(message), 'Not available now')

    def test_order_delete(self):
        order = Order.objects.create(
            user=self.user,
            book=self.book,
        )
        self.client.login(username='simple_user', password='password12Q')
        response = self.client.post(self.delete_order_url)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Order.objects.all().count(), 0)
        self.assertEqual(Book.objects.get(id=1).count, 2)

