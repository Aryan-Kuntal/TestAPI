from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
# Create your views here.

@api_view(['POST'])
def register(request):

    if request.method == 'POST':

        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():

            user = serializer.save()

            return Response({'details':serializer.data,'response':'Succesfully created','token':Token.objects.get(user=user).key},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


def landing(request):
    return render(request,'main/landing.html',{})