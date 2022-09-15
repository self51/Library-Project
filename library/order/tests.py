from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve

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

