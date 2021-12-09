from django.contrib import admin
from .models import Temperature, Weather


admin.site.register(Weather)
admin.site.register(Temperature)
