from django.urls import path
from .views import UserListCreateView, UserDetailsView, TodoListCreateView, TodoDetailsView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailsView.as_view(), name='user-details'),
    path('todos/', TodoListCreateView.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', TodoDetailsView.as_view(), name='todo-details'),
]
