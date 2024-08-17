from rest_framework import routers
from django.urls import path, include
from api import views

router = routers.DefaultRouter()

router.register(r'uf', views.UFViewSet, basename='uf')

urlpatterns = [
    path('', include(router.urls))
]
