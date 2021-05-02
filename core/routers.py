from rest_framework.routers import SimpleRouter
from core.user.viewsets import UserViewSet
from core.auth.viewsets import LoginViewSet, RegistrationViewSet


routes = SimpleRouter()

routes.register(r'user', UserViewSet, basename='user')
routes.register(r'auth/login', LoginViewSet, basename='auth-login')
routes.register(r'auth/register', RegistrationViewSet, basename='auth-register')


urlpatterns = [
    *routes.urls
]
