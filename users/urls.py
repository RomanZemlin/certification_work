from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

urlpatterns = [
    path('users/', views.UserListCreateAPIView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', views.UserRetrieveUpdateDestroyAPIView.as_view(), name='user-retrieve-update-destroy'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
