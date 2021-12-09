from django.urls import path
from graphene_django.views import GraphQLView

from . import views

from rest_framework.routers import DefaultRouter

from .views import WeatherViewSet


router = DefaultRouter(trailing_slash=False)
router.register(r'weather', WeatherViewSet, basename='weather')
urlpatterns = router.urls
