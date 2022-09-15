from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve

from authentication.views import SignUpView, account, edit_user, change_password


class TestUrl(SimpleTestCase):

    def test_signup_url_resolves(self):
        url = reverse('signup')
        self.assertEqual(resolve(url).func.view_class, SignUpView)

    def test_account_url_resolves(self):
        url = reverse('account')
        self.assertEqual(resolve(url).func, account)

    def test_edit_user_url_resolves(self):
        url = reverse('edit_user', args=[1])
        self.assertEqual(resolve(url).func, edit_user)

    def test_change_password_url_resolves(self):
        url = reverse('change_password')
        self.assertEqual(resolve(url).func, change_password)

