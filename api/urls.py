from rest_framework import routers
from django.urls import path, include

from .views.uf.single_value_view import GetUFView
from .views.uf.monthly_value_view import MonthlyValuesAPIView

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),  # Incluir las rutas del router
    path('uf/single/', GetUFView.as_view(), name='uf-single-value'),
    path('uf/monthly/', MonthlyValuesAPIView.as_view(), name='uf-monthly-value'),
]
