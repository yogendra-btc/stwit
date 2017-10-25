# import code; code.interact(local=dict(globals(), **locals()))
from django.shortcuts import render
import json
from django.http import Http404
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token  
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model 
from .serializers import UserSerializer,KeywordSerializer


class CreateUserView(APIView):

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data.get('data'))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StoreKeyword(APIView):

    def post(self, request, format=None):
        serializer = KeywordSerializer(data=request.data.get('data'))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



