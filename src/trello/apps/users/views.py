from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework import Response
from rest_framework import status
from . import serializers

class OTPView(APIView):
    def get(self,request):
        serializer = serializers.RequestOTPSerializer(data=request.query_params)
        if serializer.is_valid():
            pass
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data = serializer.errors )
    def post(self, request):
        pass