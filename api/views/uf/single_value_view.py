from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from api.utils.get_uf import get_uf

class GetUFView(APIView):

    def get(self, request):
        try:
            # Obtener los parámetros de la solicitud GET
            day = int(request.query_params.get('day', 0))
            month = int(request.query_params.get('month', 0))
            year = int(request.query_params.get('year', 0))

            # Validar los parámetros de fecha
            if not (1 <= day <= 31) or not (1 <= month <= 12):
                return Response({'error': 'El día o el mes no son válidos.'}, status=status.HTTP_400_BAD_REQUEST)
            
            # Verificar que la fecha sea posterior al 1 de enero de 2013
            minimum_date = datetime(2013, 1, 1)
            selected_date = datetime(year, month, day)

            if selected_date >= minimum_date:
                # Construir la URL y obtener el valor de la UF
                url = f'https://www.sii.cl/valores_y_fechas/uf/uf{year}.htm'
                try:
                    uf_value = get_uf(url, day, month)
                    return Response({'uf_value': uf_value, 'date': selected_date.strftime('%d/%m/%Y')})
                except RuntimeError as e:
                    return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response({'error': 'La fecha debe ser posterior al 1 de enero de 2013.'}, status=status.HTTP_400_BAD_REQUEST)

        except (ValueError, TypeError):
            return Response({'error': 'Los parámetros de fecha no son válidos.'}, status=status.HTTP_400_BAD_REQUEST)
