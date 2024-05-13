from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

class NoteListCreate(generics.ListCreateAPIView):
    # Verify if the user is authenticated
    permission_classes = [IsAuthenticated]
    serializer_class = NoteSerializer
    
    # Get the notes of the user if the user is authenticated
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user).order_by('-created_at')
    
    # Create a note if the user is authenticated
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)


class NoteDelete(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NoteSerializer
    
    # This function is used to get the notes of the user and delete the note especific for the user
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    
    
        
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

