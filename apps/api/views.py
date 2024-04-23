from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import User, Todo
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
# Create your views here.
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        print(self.request.method == "POST")
        if self.request.method == "POST":
            return RegisterSerializer
        return UserSerializer

class UserDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class TodoListCreateView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

class TodoDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]
    
class DeleteUserTodosView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        request.user.todo_set.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
