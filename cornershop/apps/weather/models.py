import uuid

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone

TEMPERATURE_MIN = -273.15
TEMPERATURE_MAX = 122.00


class Weather(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    city = models.CharField(max_length=300)
    date = models.DateField(blank=False, default=timezone.now(), null=False)
    state = models.CharField(max_length=200)
    lat = models.FloatField(validators=[MinValueValidator(-90), MaxValueValidator(90)])
    lon = models.FloatField(validators=[MinValueValidator(-180), MaxValueValidator(180)])

    class Meta:
        db_table = 'weather'

    objects = models.Manager()
    ordering = ('date',)
    list_display = ('id', 'city', 'date', 'state', 'lat', 'lon')

    FORM_CHOICES = (
        ('city', 'City'),
        ('date', 'Date'),
    )

    def __repr__(self):
        return 'Weather(id={}, date={}, city={}, lat={}, lon={}, state={})'.format(
            self.id,
            self.date,
            self.city,
            self.lat,
            self.lon,
            self.state,
        )

    @property
    def temperatures(self):
        return Temperature.objects.filter(weather=self.id)


class Temperature(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    actual = models.FloatField(
        validators=[MinValueValidator(TEMPERATURE_MIN), MaxValueValidator(TEMPERATURE_MAX)],
    )
    date = models.DateField(
        blank=False,
        default=timezone.now(),
        null=False)
    max = models.FloatField(
        blank=True,
        null=True,
        validators=[MinValueValidator(TEMPERATURE_MIN), MaxValueValidator(TEMPERATURE_MAX)],
    )
    min = models.FloatField(
        blank=True,
        null=True,
        validators=[MinValueValidator(TEMPERATURE_MIN), MaxValueValidator(22)],
    )
    weather = models.ForeignKey(Weather, db_column='weather', related_name='temperatures', on_delete=models.CASCADE)

    class Meta:
        db_table = 'temperature'
        ordering = ('date',)
        unique_together = ('id', 'weather')

    objects = models.Manager()
    list_display = ('id', 'weather', 'actual', 'date', 'max', 'min')
    FORM_CHOICES = (
        ('actual', 'Actual'),
        ('date', 'Date'),
        ('max', 'Maximum'),
        ('min', 'Minimum')
    )

    def __repr__(self):
        return 'Weather(id={}, actual={}, max={}, min={})'.format(
            '%d' % self.id,
            '%2.2f' % self.actual,
            '%2.2f' % self.max,
            '%2.2f' % self.min,
        )

    def __str__(self):
        return '%2.2f' % self.actual
