import http.client
import os
import unittest
from urllib.request import urlopen
from urllib.error import HTTPError

import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def _get(self, path):
        url = f"{BASE_URL}{path}"
        try:
            return urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            return e

    def test_api_root(self):
        response = self._get("")
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "Hello from The Calculator!\n")

    def test_api_add(self):
        response = self._get("/calc/add/2/2")
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "4")

    def test_api_add_invalid_operand(self):
        response = self._get("/calc/add/a/2")
        self.assertEqual(response.status, http.client.BAD_REQUEST)
        self.assertEqual(response.read().decode(), "Operator cannot be converted to number")

    def test_api_substract(self):
        response = self._get("/calc/substract/5/3")
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "2")

    def test_api_substract_invalid_operand(self):
        response = self._get("/calc/substract/5/x")
        self.assertEqual(response.status, http.client.BAD_REQUEST)
        self.assertEqual(response.read().decode(), "Operator cannot be converted to number")

    def test_api_multiply(self):
        response = self._get("/calc/multiply/3/4")
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "12")

    def test_api_divide(self):
        response = self._get("/calc/divide/3/2")
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "1.5")

    def test_api_divide_by_zero(self):
        response = self._get("/calc/divide/5/0")
        self.assertEqual(response.status, http.client.BAD_REQUEST)
        self.assertEqual(response.read().decode(), "Division by zero is not possible")

    def test_api_power(self):
        response = self._get("/calc/power/2/3")
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "8")

    def test_api_sqrt(self):
        response = self._get("/calc/sqrt/9")
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "3.0")

    def test_api_sqrt_negative(self):
        response = self._get("/calc/sqrt/-1")
        self.assertEqual(response.status, http.client.BAD_REQUEST)
        self.assertEqual(response.read().decode(), "Square root of negative numbers is not possible")

    def test_api_log(self):
        response = self._get("/calc/log/10")
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "1.0")

    def test_api_log_invalid_operand(self):
        response = self._get("/calc/log/zero")
        self.assertEqual(response.status, http.client.BAD_REQUEST)
        self.assertEqual(response.read().decode(), "Operator cannot be converted to number")

    def test_api_log_zero(self):
        response = self._get("/calc/log/0")
        self.assertEqual(response.status, http.client.BAD_REQUEST)
        self.assertEqual(response.read().decode(), "Logarithm of negative numbers or zero is not possible")
