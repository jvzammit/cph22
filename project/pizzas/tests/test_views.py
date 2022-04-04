from django.test import Client, TestCase
from django.urls import reverse
from pizzas.tests.utils import load_data


class HomeViewTest(TestCase):
    def test_home(self):
        load_data()
        client = Client()
        with self.assertNumQueries(2):
            response = client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
