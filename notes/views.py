from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import *
from rest_framework.decorators import permission_classes,api_view,action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets
from .models import Note
from .serializer import NoteSerializer


@permission_classes((AllowAny,))
class register(APIView):   #Register a new user
    def post(self, request):
            if request.data["username"] is None or request.data["email"] is None or request.data["password"] is None:  
                return Response({
                    "ERROR" : "Please Enter The Details For Registration"
                },status= status.HTTP_400_BAD_REQUEST)
            user = User(username = request.data["username"],password = request.data["password"], email = request.data["email"])
            if user:
                user.set_password(request.data["password"])
                user.save()
                return Response({
                    "success": "User registered succesfully"
                }, status = status.HTTP_202_ACCEPTED)
            else:
                return Response({
                    "ERROR" : "Encountered an error"
                },status = status.HTTP_400_BAD_REQUEST)

@permission_classes((AllowAny, ))
class login(APIView):   #logins the user
    def post(self,request):
        if not request.data:   #validation
            return Response({
                "ERROR": "Please provide a username and password"
            },status = status.HTTP_400_BAD_REQUEST)
        username = request.data["username"]    #extracting data from JSON data
        password = request.data["password"]
        if username is None or password is None:    #validation
            return Response({
                "ERROR": "Required fields are not provided"
            }, status = status.HTTP_400_BAD_REQUEST)
        user = authenticate(username = username, password = password) #authentication
        return Response({
            "Messege" : "Succesfullly logged in"
        }, status = status.HTTP_200_OK)
    
@permission_classes((IsAuthenticated, ))
class NoteViewSet(viewsets.ModelViewSet):    #creates and retrives notes
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

@api_view(('GET',))
@permission_classes((IsAuthenticated, ))      
def recieved(request):                      #retrieves inbox of the current user
    user = request.user
    note = Note.objects.filter(recipent = user)
    note_ser = NoteSerializer(note, many=True)
    return Response(note_ser.data)