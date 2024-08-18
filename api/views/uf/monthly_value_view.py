from datetime import datetime
from typing import Dict, List, Union
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.constants import MINIMUM_DATE
from api.utils.get_uf import get_uf

class MonthlyValuesAPIView(APIView):
    """
    Vista para obtener todos los valores de la UF para un mes y año específicos.
    """
    def get(self, request) -> Response:
        """
        Maneja una solicitud GET para obtener los valores de la UF para un mes y año específicos.

        Parámetros:
        - month (int): Mes (1-12).
        - year (int): Año (>= 2013).

        Respuestas:
        - 200 OK: Lista de valores UF para cada día del mes.
        - 400 Bad Request: Parámetros inválidos o fecha anterior al 1 de enero de 2013.
        - 500 Internal Server Error: Error al obtener los valores de la UF.
        """
        try:
            # Obtener los parámetros de la solicitud GET
            month: int = int(request.query_params.get('month', 0))
            year: int = int(request.query_params.get('year', 0))
            
            # Validar el mes y año
            if not (1 <= month <= 12) or year < 2013:
                return Response({'error': 'El mes o el año no son válidos.'}, status=status.HTTP_400_BAD_REQUEST)
            
            # Verificar que la fecha sea posterior al 1 de enero de 2013
            selected_date = datetime(year, month, 1)

            if selected_date < MINIMUM_DATE:
                return Response({'error': 'La fecha debe ser posterior al 1 de enero de 2013.'}, status=status.HTTP_400_BAD_REQUEST)

            # Construir la URL base
            url: str = f'https://www.sii.cl/valores_y_fechas/uf/uf{year}.htm'
            
            # Obtener todos los valores UF para el mes dado
            try:
                uf_values: List[Dict[str, Union[str, float]]] = []
                for day in range(1, 32):
                    try:
                        # Verificar si el día es válido para el mes
                        datetime(year, month, day)
                        uf_value: Union[str, float] = get_uf(url, day, month)
                        uf_values.append({'date': f'{day:02d}/{month:02d}/{year}', 'uf_value': uf_value})
                    except ValueError:
                        # Día no válido para el mes
                        break
                return Response(uf_values)
            except RuntimeError as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
        except (ValueError, TypeError):
            return Response({'error': 'Los parámetros de fecha no son válidos.'}, status=status.HTTP_400_BAD_REQUEST)
