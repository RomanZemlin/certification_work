from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter


users_router = SimpleRouter()

# В роутер регистрируем ViewSet, который импортирован из Djoser
users_router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(users_router.urls)),
]

# https://djoser.readthedocs.io/en/latest/base_endpoints.html
# GET "users/" — список профилей пользователей
# POST "users/" — регистрация пользователя
# GET, PATCH, DELETE "users/{id}" — в соответствии с REST и необходимыми permissions (для администратора)
# GET PATCH "users/me" — получение и изменение своего профиля
# POST "users/set_password" — ручка для изменения пароля
# POST "users/reset_password" — ручка для направления ссылки сброса пароля на email*
# POST "users/reset_password_confirm" — ручка для сброса своего пароля*
