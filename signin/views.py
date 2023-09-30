from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

@api_view(['POST'])
def sign_in(request):
  """
  登入
  """
  return Response({'message':'success'},status=status.HTTP_201_CREATED)
