from django.test import TestCase
from django.urls import reverse

# Create your tests here.

from .models import Clients


class ClientsModelTest(TestCase):
    def setUp(self):
        Clients.objects.create(
            name='Alex',
            email='alex@alex.ru',
            phone='8911',
        )

    def test_fields_content(self):
        client = Clients.objects.get(id=1)
        expected_object_name = f'{client.name}'
        self.assertEqual(expected_object_name, 'Alex')
        expected_object_email = f'{client.email}'
        self.assertEqual(expected_object_email, 'alex@alex.ru')
        expected_object_phone = f'{client.phone}'
        self.assertEqual(expected_object_phone, '8911')


class ClientsPageViewTest(TestCase):
    def setUp(self):
        Clients.objects.create(
            name='Irina',
            email='irina@irina.ru',
            phone='8921',
        )

    def test_view_url_exists_at_proper_location(self):
        response = self.client.get('/clients.html')
        self.assertEqual(response.status_code, 200)
