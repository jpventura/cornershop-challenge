from copy import deepcopy

from django.urls import reverse

from os import path

from rest_framework import status
from rest_framework.test import APITestCase

import json


FIXTURES_DIR = path.join(
    path.dirname(path.dirname(path.abspath(__file__))),
    'fixtures'
)

RESPONSE_EMPTY_PAGE = {
    'count': 0,
    'next': None,
    'previous': None,
    'results': []
}


class WeatherAPTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('weather-list')

        self.response = deepcopy(RESPONSE_EMPTY_PAGE)

        with open(path.join(FIXTURES_DIR, 'weather.json')) as f:
            self.body = json.load(f)
            self.response['results'].extend([self.client.post(self.url, w, format='json').data for w in self.body])
            self.response['count'] = len(self.response['results'])
