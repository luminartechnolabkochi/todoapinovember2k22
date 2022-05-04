from django.shortcuts import render
from api.models import todos
# Create your views here.

from rest_framework.response import Response
# api/v1/todos =>get
from rest_framework import status
from rest_framework.views import APIView
import json
class Todos(APIView):
    def get(self,request,*args,**kwargs):
        with open("/home/luminar/Desktop/djangoprojects/django_nov_2k22/djangoworks/todoapi/api/todos.json","r") as f:
            data=json.load(f)
        return Response({"data":data},status=status.HTTP_200_OK)


