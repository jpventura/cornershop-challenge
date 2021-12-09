from django.conf import settings
from django.urls import path, re_path, reverse_lazy
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import RedirectView

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_swagger.views import get_swagger_view

from cornershop.apps.users.views import UserCreateViewSet, UserViewSet


router = DefaultRouter(trailing_slash=True)
router.register(r'users', UserViewSet)
router.register(r'users', UserCreateViewSet)

endpoints_patterns = [
    path('api/v1/', include(router.urls)),
]

schema_view = get_swagger_view(
    patterns=endpoints_patterns,
    title='Cornershop Weather API',
)

urlpatterns = [
    *endpoints_patterns,

    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Open API 3.x Schema
    path('docs/', schema_view, name='swagger'),

    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('swagger'), permanent=False)),
] + static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT,
) + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
