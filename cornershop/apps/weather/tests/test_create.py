from django.urls import reverse

from rest_framework import status

from cornershop.apps.weather.tests import WeatherAPTestCase


class WeatherPostTestCase(WeatherAPTestCase):

    def test_with_existing_record(self):
        url = reverse('weather-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('results'), self.response['results'])
