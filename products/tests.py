from rest_framework.test import APITestCase
from rest_framework import status

from products.models import Product


class ProductTests(APITestCase):
    def setUp(self):
        self.base_url = "/api/v1/products/"

    def test_list_products(self):
        """
        Ensure we can list products.
        """
        url = self.base_url
        data = {
            "reference": "123456",
            "name": "Product 1",
            "description": "This is a product",
            "base_price": 100.0,
            "tax_rate": 0.21,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, 201)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        response_data = response.data["body"]
        self.assertEqual(len(response_data), 1)
        self.assertEqual(response_data[0]["reference"], "123456")
        self.assertEqual(response_data[0]["name"], "Product 1")
        self.assertEqual(float(response_data[0]["base_price"]), 100.0)
        self.assertEqual(float(response_data[0]["tax_rate"]), 0.21)

    def test_create_product(self):
        """
        Ensure we can create a new product object.
        """

        url = self.base_url
        data = {
            "reference": "ART002",
            "name": "New Product",
            "description": "A new product",
            "base_price": 150.00,
            "tax_rate": 18.00,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get(reference="ART002").name, "New Product")

    def test_get_product(self):
        """
        Ensure we can get a product object.
        """
        url = self.base_url
        data = {
            "reference": "12345",
            "name": "closet",
            "description": "Buen closet",
            "base_price": 1200.00,
            "tax_rate": 21.00,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, 201)
        product_data = response.data["body"]
        product_id = product_data["id"]
        url = self.base_url + f"{product_id}/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(product_data["reference"], "12345")
        self.assertEqual(product_data["name"], "closet")
        self.assertEqual(product_data["description"], "Buen closet")
        self.assertEqual(float(product_data["base_price"]), 1200)
        self.assertEqual(float(product_data["tax_rate"]), 21.00)

    def test_update_product(self):
        """
        Ensure we can update a product object.
        """
        url = self.base_url
        data = {
            "reference": "123456",
            "name": "Product 1",
            "description": "This is a product",
            "base_price": 100.0,
            "tax_rate": 0.21,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, 201)
        response_data = response.data["body"]
        product_id = response_data["id"]
        url = self.base_url + f"{product_id}/"
        data = {
            "reference": "123456",
            "name": "Product 1",
            "description": "This is a product",
            "base_price": 200.0,
            "tax_rate": 0.21,
        }
        response = self.client.put(url, data, format="json")
        response_data = response.data["body"]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data["reference"], "123456")
        self.assertEqual(response_data["name"], "Product 1")
        self.assertEqual(response_data["description"], "This is a product")
        self.assertEqual(float(response_data["base_price"]), 200.0)
        self.assertEqual(float(response_data["tax_rate"]), 0.21)
