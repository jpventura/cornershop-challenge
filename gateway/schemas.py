import graphene

from cornershop.apps.weather.schemas import WeatherQuery


class Query(WeatherQuery):
    pass


schema = graphene.Schema(query=Query)
