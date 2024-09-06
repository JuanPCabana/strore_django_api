from rest_framework import status
from rest_framework.test import APITestCase

from orders.models import Order
from products.models import Product


class OrderTests(APITestCase):
    def setUp(self):
        self.base_url = "/api/v1/orders/"
        self.products_url = "/api/v1/products/"

        def create_products():

            data = {
                "reference": "ART001",
                "name": "New Product",
                "description": "A new product",
                "base_price": 150.00,
                "tax_rate": 18.00,
            }
            response = self.client.post(self.products_url, data, format="json")
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(Product.objects.count(), 1)
            self.assertEqual(
                Product.objects.get(reference="ART001").name, "New Product"
            )

            data = {
                "reference": "ART002",
                "name": "New new Product",
                "description": "A new new product",
                "base_price": 200.00,
                "tax_rate": 25.00,
            }
            response = self.client.post(self.products_url, data, format="json")
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(Product.objects.count(), 2)
            self.assertEqual(
                Product.objects.get(reference="ART001").name, "New Product"
            )

        self.create_products = create_products

    def test_list_orders(self):
        """
        Ensure we can list orders.
        """
        self.create_products()

        data = {
            "items": [
                {"product_id": 1, "quantity": 2},
                {"product_id": 2, "quantity": 1},
            ]
        }

        response = self.client.post(self.base_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_data = response.data["body"]
        self.assertEqual(response_data["id"], 1)
        self.assertEqual(len(response_data["items"]), 2)
        self.assertEqual(response_data["items"][0]["product"]["reference"], "ART001")
        self.assertEqual(response_data["items"][0]["product"]["name"], "New Product")
        self.assertEqual(response_data["items"][0]["quantity"], 2)
        self.assertEqual(response_data["items"][1]["product"]["reference"], "ART002")
        self.assertEqual(
            response_data["items"][1]["product"]["name"], "New new Product"
        )
        self.assertEqual(response_data["items"][1]["quantity"], 1)

    def test_create_order(self):
        """
        Ensure we can create a new order object.
        """
        self.create_products()

        data = {
            "items": [
                {"product_id": 1, "quantity": 2},
                {"product_id": 2, "quantity": 1},
            ]
        }

        response = self.client.post(self.base_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.get(id=1).items.count(), 2)

    def test_get_order(self):
        """
        Ensure we can get an order object.
        """

        self.create_products()

        data = {
            "items": [
                {"product_id": 1, "quantity": 2},
                {"product_id": 2, "quantity": 1},
            ]
        }

        response = self.client.post(self.base_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        order_data = response.data["body"]
        order_id = order_data["id"]
        url = self.base_url + f"{order_id}/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.data["body"]
        self.assertEqual(response_data["id"], 1)
        self.assertEqual(len(response_data["items"]), 2)
        self.assertEqual(response_data["items"][0]["product"]["reference"], "ART001")
        self.assertEqual(response_data["items"][0]["product"]["name"], "New Product")
        self.assertEqual(response_data["items"][0]["quantity"], 2)
        self.assertEqual(response_data["items"][1]["product"]["reference"], "ART002")
        self.assertEqual(
            response_data["items"][1]["product"]["name"], "New new Product"
        )
        self.assertEqual(response_data["items"][1]["quantity"], 1)

    def test_update_order(self):
        """
        Ensure we can update an order object.
        """
        self.create_products()

        data = {
            "items": [
                {"product_id": 1, "quantity": 2},
                {"product_id": 2, "quantity": 1},
            ]
        }

        response = self.client.post(self.base_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        order_data = response.data["body"]
        order_id = order_data["id"]
        url = self.base_url + f"{order_id}/"
        data = {
            "items": [
                {"product_id": 1, "quantity": 3},
                {"product_id": 2, "quantity": 2},
            ]
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.data["body"]
        self.assertEqual(response_data["id"], 1)
        self.assertEqual(len(response_data["items"]), 2)
        self.assertEqual(response_data["items"][0]["product"]["reference"], "ART001")
        self.assertEqual(response_data["items"][0]["product"]["name"], "New Product")
        self.assertEqual(response_data["items"][0]["quantity"], 3)
        self.assertEqual(response_data["items"][1]["product"]["reference"], "ART002")
        self.assertEqual(
            response_data["items"][1]["product"]["name"], "New new Product"
        )
        self.assertEqual(response_data["items"][1]["quantity"], 2)
