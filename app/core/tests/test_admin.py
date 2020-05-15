from django.test import TestCase, Client
from django.contrib.auth import get_user_model
# from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@test.com',
            password='12345@'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@test.com',
            password='12345@',
            name='Test User'
        )
        self.client.force_login(self.user)

    # def test_users_listed(self):
    #     """Test that users are listed on user page"""
    #     url = reverse('admin:core_user_changelist')
    #     print(url)
    #     res = self.client.get(url)
    #     print(res)
    #     self.assertContains(res, self.user.name)
    #     self.assertContains(res, self.user.email)
