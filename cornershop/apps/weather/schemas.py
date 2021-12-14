from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

import graphene

from cornershop.apps.weather import models


class TemperatureType(DjangoObjectType):
    class Meta:
        model = models.Temperature
        fields = ('id', 'actual', 'max', 'min')

    value = graphene.Float(required=True)


class WeatherNode(DjangoObjectType):
    class Meta:
        model = models.Weather

        filter_fields = ('id', 'city', 'date', 'state', 'lat', 'lon')

        interfaces = (relay.Node,)


class WeatherQuery(graphene.ObjectType):
    weather = relay.Node.Field(WeatherNode)
    weathers = DjangoFilterConnectionField(WeatherNode)

    def resolve_weather(self, info, id):
        return models.Weather.objects.get(id=int(id))


schema = graphene.Schema(query=WeatherQuery)
