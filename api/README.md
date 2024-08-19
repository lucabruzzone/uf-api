# API de Valores UF

Bienvenido a la API de Valores UF.

## Descripción

Esta API proporciona acceso a los valores de la Unidad de Fomento (UF) para fechas específicas y para meses completos. Los valores se obtienen desde el sitio web oficial del Servicio de Impuestos Internos (SII).

## SERVIDORES

- **Desarrollo**: http://127.0.0.1:8000

- **Producción**: https://ufapi.onrender.com

## Endpoints

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
