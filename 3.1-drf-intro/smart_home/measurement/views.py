
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from .models import Measurement, Sensor
from .serializers import MeasurementAddSerializer, SensorDetailSerializer, SensorSerializer


class SensorListView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorDetailView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementAddSerializer
