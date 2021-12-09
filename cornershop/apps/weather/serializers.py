from rest_framework import serializers
from .models import Weather, Temperature

ISO_DATE_FORMAT = '%Y-%m-%d'

TEMPERATURE_MIN = -273.15
TEMPERATURE_MAX = 122.00


class TemperatureSerializer(serializers.BaseSerializer):
    def update(self, instance, validated_data):
        Temperature.objects.update(**validated_data)

    def __init__(self, *args, **kwargs):
        super(TemperatureSerializer, self).__init__(*args, **kwargs)

    def to_internal_value(self, data):
        if type(data) in [int, float, str]:
            data = {'actual': float(data)}

        if 'actual' not in data:
            raise serializers.ValidationError({
                'actual': 'This field is required a temperature.'
            })

        return data

    def to_representation(self, instance):
        return instance.actual

    def create(self, validated_data):
        return Temperature.objects.create(**validated_data)


class WeatherSerializer(serializers.ModelSerializer):
    temperatures = TemperatureSerializer(many=True)

    class Meta:
        model = Weather
        fields = ('id', 'city', 'date', 'state', 'lat', 'lon', 'temperatures')

    def create(self, validated_data):
        temperatures = validated_data.pop('temperatures')
        weather = Weather.objects.create(**validated_data)

        for t in temperatures:
            Temperature.objects.create(
                weather=weather,
                **WeatherSerializer.format_temperature(t)
            )

        return weather

    @classmethod
    def format_temperature(cls, temperature):
        return {'actual': float(temperature)} if type(temperature) in [int, float, str] else temperature
