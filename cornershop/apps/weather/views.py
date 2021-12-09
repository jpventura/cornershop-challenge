from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny

from cornershop.apps.weather.models import Temperature, Weather
from cornershop.apps.weather.serializers import TemperatureSerializer, WeatherSerializer


@permission_classes((AllowAny, ))
class TemperatureViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['temperature']

    ordering = ['temperature']
    ordering_fields = ['id', 'weather',]

    queryset = Temperature.objects.all()

    serializer_class = TemperatureSerializer
    
    class Meta:
        fields = '__all__'
        model = Temperature


@permission_classes((AllowAny, ))
class WeatherViewSet(viewsets.ModelViewSet):
    filter_backends = (SearchFilter, OrderingFilter,)

    ordering = ('id')
    ordering_fields = ('id', 'date')

    queryset = Weather.objects.all()

    # Ensure case-insensitive match for city
    search_fields = ('city', '=date')
    serializer_class = WeatherSerializer

    def get_queryset(self):
        city = self.request.query_params.get('city', None)

        print(self.request)

        if city:
            return self.queryset.filter(city=city)

        return self.queryset

    class Meta:
        fields = '__all__'
        model = Weather
