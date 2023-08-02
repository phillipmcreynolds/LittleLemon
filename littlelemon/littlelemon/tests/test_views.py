from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token  # Import Token model
from django.contrib.auth.models import User

from Restaurant.models import Menu


class MenuViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='c3mpl5xscRt')
        self.token = Token.objects.create(user=self.user)

        Menu.objects.create(title="Fish Soup", price=10, inventory=5)
        Menu.objects.create(title="PBJ", price=2, inventory=10)
        Menu.objects.create(title="Berry Pie", price=3, inventory=5)

    def test_get_all(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        url = '/restaurant/menu-items/'
        response = client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 3)

        # Check that the response data contains the expected menu items
        expected_menu_titles = ["Fish Soup", "PBJ", "Berry Pie"]
        for menu_item, expected_title in zip(response.data, expected_menu_titles):
            self.assertEqual(menu_item['Title'], expected_title)