from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status


class CalculationTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_addition(self):
        url = '/add/'
        response = self.client.get(url, {'a': 5, 'b': 3})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['operation'], 'add')
        self.assertEqual(response.json()['result'], 8)

    def test_subtraction(self):
        url = '/subtract/'
        response = self.client.get(url, {'a': 10, 'b': 3})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['operation'], 'subtract')
        self.assertEqual(response.json()['result'], 7)

    def test_multiplication(self):
        url = '/multiply/'
        response = self.client.get(url, {'a': 4, 'b': 5})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['operation'], 'multiply')
        self.assertEqual(response.json()['result'], 20)

    def test_divide(self):
        url = '/divide/'
        response = self.client.get(url, {'a': 10, 'b': 2})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['operation'], 'divide')
        self.assertEqual(response.json()['result'], 5)

    def test_divide_by_zero(self):
        url = '/divide/'
        response = self.client.get(url, {'a': 10, 'b': 0})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json()['error'], 'Cannot divide by zero')

    def test_invalid_input(self):
        url = '/add/'
        response = self.client.get(url, {'a': 'abc', 'b': 3})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json()['error'], 'Invalid input for a or b')
