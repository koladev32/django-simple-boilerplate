from rest_framework.routers import SimpleRouter
from user.viewsets import UserViewSet


routes = SimpleRouter()

routes.register(r'user', UserViewSet, basename='user')


urlpatterns = [
    *routes.urls
]
