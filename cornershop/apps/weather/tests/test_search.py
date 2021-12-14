from copy import deepcopy

from rest_framework import status

from cornershop.apps.weather.tests import WeatherAPTestCase


class WeatherSearchTestCase(WeatherAPTestCase):

    # def test_with_no_results(self):
    #     response = self.client.get(self.url, {'city': 'Tokyo'}, format='json')
    #
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data['count'], 0)

    def test_with_more_than_one_city(self):
        response = self.client.get(self.url, kwargs={'city': 'moscow'}, format='json')

        print(response.data)


        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)

    #
    # def test_asc_order_list_matches(self):
    #     weather_response = deepcopy(self.response)
    #     weather_response['results'] = sorted(
    #         self.response['results'],
    #         key=lambda weather: weather['date'],
    #         reverse=True
    #     )
    #
    #     response = self.client.get(self.url, {'sort': 'date'}, format='json')
    #
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data, weather_response)
    #
    # def test_desc_order_list_matches(self):
    #     weather_response = deepcopy(self.response)
    #     weather_response['results'] = sorted(
    #         self.response['results'],
    #         key=lambda weather: weather['date'],
    #         reverse=True
    #     )
    #
    #     response = self.client.get(self.url, {'sort': '-date'}, format='json')
    #
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data, weather_response)
