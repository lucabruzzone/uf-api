# API de Valores UF

Esta API proporciona información sobre el valor de la Unidad de Fomento (UF) en Chile. Permite consultar el valor de la UF para un día específico o para todos los días de un mes en particular.

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

### Estructura de carpetas

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
├── build.sh
├── manage.py
├── README.md
├── requirements.txt

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

Sirviendo en: http://127.0.0.1:8000

## Uso

### Endpoints Disponibles

- **Obtener el valor UF para un día específico**: Permite consultar el valor de la UF para una fecha específica (día, mes y año).
- **Obtener los valores UF para un mes específico**: Permite consultar los valores de la UF para todos los días de un mes y año específicos.

### URL BASE

```bash
https://ufapi.onrender.com
```

### 1. Obtener el valor de la UF para una fecha específica

- **RUTA**: `/api/uf/single/`
- **Método**: `GET`
- **Descripción**: Obtiene el valor de la UF para una fecha específica.

#### Parámetros de Consulta

- `day` (int): Día del mes (1-31).
- `month` (int): Mes (1-12).
- `year` (int): Año (YYYY).

#### Ejemplo de Solicitud

```http
GET http://127.0.0.1:8000/api/uf/single/?day=19&month=8&year=2024
```

#### Respuestas

- 200 OK:

```json
{
  "uf_value": "22.837,06",
  "date": "19/08/2024"
}
```

- 400 Bad Request:

```json
{
  "error": "El día o el mes no son válidos."
}
```

```json
{
  "error": "La fecha debe ser posterior al 1 de enero de 2013."
}
```

```json
{
  "error": "Los parámetros de fecha no son válidos."
}
```

- 500 Internal Error:

```json
{
  "error": "Error al obtener el valor de la UF."
}
```

### 2. Obtener todos los valores de la UF para un mes y año específicos

- **RUTA**: `/api/uf/monthly/`
- **Método**: `GET`
- **Descripción**: Obtiene todos los valores de la UF para un mes y año específicos.

#### Parámetros de Consulta

- `month` (int): Mes (1-12).
- `year` (int): Año (YYYY).

#### Ejemplo de Solicitud

```http
GET http://127.0.0.1:8000/api/uf/monthly/?month=8&year=2024
```

#### Respuestas

- 200 OK:

```json
[
  {"date": "01/08/2024", "uf_value": "22.837,06"},
  {"date": "02/08/2024", "uf_value": "22.847,12"},
  ...
  {"date": "31/08/2024", "uf_value": "22.890,34"}
]

```

- 400 Bad Request:

```json
{
  "error": "El mes o el año no son válidos."
}
```

```json
{
  "error": "La fecha debe ser posterior al 1 de enero de 2013."
}
```

```json
{
  "error": "Los parámetros de fecha no son válidos."
}
```

- 500 Internal Error:

```json
{
  "error": "Error al obtener los valores de la UF."
}
```
