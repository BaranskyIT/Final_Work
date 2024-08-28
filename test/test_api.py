import unittest
import requests
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from constants import BASE_URL

# class TestAPI(unittest.TestCase):
#     def test_api_status(self):
#         response = requests.get(BASE_URL)
#         self.assertEqual(response.status_code, 200, "API не возвращает статус 200")

# if __name__ == '__main__':
#     unittest.main()
