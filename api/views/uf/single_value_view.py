from datetime import datetime
from typing import Union
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.constants import MINIMUM_DATE
from api.utils.get_uf import get_uf

class GetUFView(APIView):
    """
    Vista para obtener el valor de la UF para una fecha específica.
    """
    def get(self, request) -> Response:
        """
        Maneja una solicitud GET para obtener el valor de la UF de un día específico.

        Parámetros:
        - day (int): Día del mes (1-31).
        - month (int): Mes (1-12).
        - year (int): Año (YYYY).

        Respuestas:
        - 200 OK: Valor de la UF y fecha.
        - 400 Bad Request: Parámetros inválidos o fecha anterior al 1 de enero de 2013.
        - 500 Internal Server Error: Error al obtener el valor de la UF.
        """
        try:
            # Obtener los parámetros de la solicitud GET
            day: int = int(request.query_params.get('day', 0))
            month: int = int(request.query_params.get('month', 0))
            year: int = int(request.query_params.get('year', 0))

            # Validar los parámetros de fecha
            if not (1 <= day <= 31) or not (1 <= month <= 12):
                return Response({'error': 'El día o el mes no son válidos.'}, status = status.HTTP_400_BAD_REQUEST)
            
            # Verificar que la fecha sea posterior al 1 de enero de 2013
            selected_date = datetime(year, month, day)

            if selected_date >= MINIMUM_DATE:
                # Construir la URL y obtener el valor de la UF
                url: str = f'https://www.sii.cl/valores_y_fechas/uf/uf{year}.htm'
                try:
                    uf_value: Union[str, float] = get_uf(url, day, month)
                    return Response({'uf_value': uf_value, 'date': selected_date.strftime('%d/%m/%Y')})
                except RuntimeError as e:
                    return Response({'error': str(e)}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response({'error': 'La fecha debe ser posterior al 1 de enero de 2013.'}, status = status.HTTP_400_BAD_REQUEST)

        except (ValueError, TypeError):
            return Response({'error': 'Los parámetros de fecha no son válidos.'}, status = status.HTTP_400_BAD_REQUEST)
