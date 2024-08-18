# Proyecto Desafío Técnico

Desafío técnico para el puesto de `desarrollador backend`

## Descripción

Este proyecto consta de una única aplicación, una `API` para poder consultar los valores de la Unidad de Fomento (UF) por día y por mes, a partir del 1 de Enero de 2013.

## Implementación

### Dependencias

Asegúrate de tener las siguientes dependencias instaladas:

- `Django`
- `djangorestframework`
- `Requests`
- `BeautifulSoup`
- `djangorestframework`

### Instalación

Para instalar las dependencias necesarias, ejecuta:

```bash
pip install -r requirements.txt
```

### Configuración del Proyecto

Después de instalar las dependencias, asegúrate de que tu proyecto está correctamente configurado. Esto incluye:

1. Configuración de las rutas: Asegúrate de haber agregado las rutas de tu API en el archivo urls.py de la carpeta `api` correspondiente. Un ejemplo de configuración podría ser el siguiente:

```python
# urls.py
from rest_framework import routers
from django.urls import path, include

from .views.uf.single_value_view import GetUFView
from .views.uf.monthly_value_view import MonthlyValuesAPIView

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('uf/single/', GetUFView.as_view(), name='uf-single-value'),
    path('uf/monthly/', MonthlyValuesAPIView.as_view(), name='uf-monthly-value'),
]
```

### Ejecutar el Servidor

```bash
python manage.py runserver
```

## Desarrollo

### Vistas

El proyecto está dividido en múltiples vistas, cada una responsable de manejar solicitudes específicas. Aquí se detalla la funcionalidad de las vistas principales:

1. `GetUFView` (single_value_view.py)
2. `MonthlyValuesAPIView` (monthly_value_view.py)

Para información detallada sobre las vistas, revisa el `README.md` que encontrarás en la carpeta `api`

### Estructura de la aplicación

```text
.
├── api/
│   ├── migrations/
│   ├── utils/
│   │   └── get_uf.py
│   ├── views/
│   │   └── uf/
│   │       ├── __init__.py
│   │       ├── monthly_value_view.py
│   │       └── single_value_view.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── constants.py
│   ├── models.py
│   ├── README.md
│   ├── tests.py
│   └── urls.py
├── uf_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── .gitignore
├── manage.py
├── README.md
├── requirements.txt

```
