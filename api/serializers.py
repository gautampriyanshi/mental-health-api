from rest_framework import serializers

class PredictSerializer(serializers.Serializer):
    message = serializers.CharField()
