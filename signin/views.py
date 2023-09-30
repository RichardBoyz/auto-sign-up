from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from signin.signup_service import main
@api_view(['POST'])
def sign_in(request):
  """
  登入
  """
  try:
    main()
  except Exception as e:
    print(e)
    return Response({'message':'fail'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  return Response({'message':'success'},status=status.HTTP_201_CREATED)
