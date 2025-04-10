from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from animals_app.views import BreedViewSet, DogViewSet

router = routers.DefaultRouter()
router.register(r'breeds', BreedViewSet)
router.register(r'dogs', DogViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
