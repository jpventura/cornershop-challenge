from django.urls import reverse

from rest_framework import status

from cornershop.apps.weather.tests import WeatherAPTestCase, RESPONSE_EMPTY_PAGE


class WeatherListTestCase(WeatherAPTestCase):
    def test_list_all(self):
        response = self.client.get(self.url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('results'), self.response['results'])

    def test_list_by_id(self):
        for weather in self.response['results']:
            url = reverse('weather-detail', kwargs={'pk': weather['id']})
            response = self.client.get(url, format='json')
            self.assertEqual(response.data, weather)
