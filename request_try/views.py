from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import response, status
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.

class EmptyView(APIView):
    def get(self, request):
        print(request.META.get('HTTP_X_FORWARDED_FOR'))
        print(request.META.get('REMOTE_ADDR'))
        return JsonResponse({},status=status.HTTP_200_OK)
