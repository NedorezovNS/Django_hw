from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, related_name="measurements", on_delete=models.CASCADE)
    temperature = models.DecimalField(max_digits=4, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True)
