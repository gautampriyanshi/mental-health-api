from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import joblib
import os
from .serializers import PredictSerializer

# Load model once when server starts
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, 'api', 'model', 'mental_health_risk_model.pkl')
model = joblib.load(model_path)

class PredictView(APIView):
    def post(self, request):
        serializer = PredictSerializer(data=request.data)
        if serializer.is_valid():
            message = serializer.validated_data['message']
            prediction = model.predict([message])[0]
            return Response({"prediction": prediction})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.
