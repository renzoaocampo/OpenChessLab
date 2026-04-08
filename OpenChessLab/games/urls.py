from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from games.views import GameViewSet, PlayerViewSet

router = routers.DefaultRouter()
router.register(r'players', PlayerViewSet)
router.register(r'games', GameViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
