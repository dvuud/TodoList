from django.urls import path
from .views import UserListCreateView, UserDetailsView, TodoListCreateView, TodoDetailsView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView 

urlpatterns = [

    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailsView.as_view(), name='user-details'),
    path('todos/', TodoListCreateView.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', TodoDetailsView.as_view(), name='todo-details'),

]
