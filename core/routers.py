from rest_framework.routers import SimpleRouter
from core.user.viewsets import UserViewSet
from core.auth.viewsets import LoginViewSet


routes = SimpleRouter()

routes.register(r'user', UserViewSet, basename='user')
routes.register(r'login', LoginViewSet, basename='login')


urlpatterns = [
    *routes.urls
]
