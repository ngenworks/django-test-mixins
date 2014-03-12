"""
The following are used in conjunction with Django Rest Framework.
"""

import json

from rest_framework.test import APITestCase


class APITestBase(APITestCase):
    """
    Extends :class:``APITestCase``
    """

    def get_json(self, response):
        """
        Example:

        response = self.client.get('some-url')
        json = self.get_json(response)
        """
        return json.loads(response.content)
