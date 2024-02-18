from .models import Measurement, Sensor
from rest_framework import serializers


class SensorSerializer(serializers.ModelSerializer):

    class Meta():
        model = Sensor
        fields = ['id', 'name', 'description']


class MeasurementSerializer(serializers.ModelSerializer):

    class Meta():
        model = Measurement
        fields = ['temperature', 'created_at']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta():
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']


class MeasurementAddSerializer(serializers.ModelSerializer):

    class Meta():
        model = Measurement
        fields = ['sensor', 'temperature', 'created_at']
