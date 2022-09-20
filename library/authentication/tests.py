from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve

from django.contrib.auth.models import User
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


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('signup')
        self.account_url = reverse('account')
        self.change_password_url = reverse('change_password')
        self.user = User.objects.create_user(
            username = 'simple_user',
            password = 'password12Q',
        )

    def test_signup_view(self):
        response = self.client.get(self.signup_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_account_view(self):
        response = self.client.get(self.account_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/account.html')

    def test_edit_user_get(self):
        response = self.client.get(reverse('edit_user', args=[4]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/account_form.html')

    def test_edit_user_post(self):
        response = self.client.post(reverse('edit_user', args=[5]), {
            'first_name': 'Name'
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.get(id=5).first_name, 'Name')

    def test_change_password_get(self):
        response = self.client.get(self.change_password_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/change_password.html')

    def test_change_password_post(self):
        self.client.login(username='simple_user', password='password12Q')
        response = self.client.post(self.change_password_url, {
            'old_password': 'password12Q',
            'new_password1': 'password12V',
            'new_password2': 'password12V',
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.login(username='simple_user', password='password12V'), True)