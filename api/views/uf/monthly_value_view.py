# api/views/uf/monthly_values_view.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from api.utils.get_uf import get_uf

class MonthlyValuesAPIView(APIView):
    def get(self, request):
        try:
            # Obtener los parámetros de la solicitud GET
            month = int(request.query_params.get('month', 0))
            year = int(request.query_params.get('year', 0))
            
            # Validar el mes y año
            if not (1 < month < 12) or 2013 > year:
                return Response({'error': 'El mes o el año no son válidos.'}, status=status.HTTP_400_BAD_REQUEST)
            
            # Verificar que la fecha sea posterior al 1 de enero de 2013
            start_date = datetime(2013, 1, 1)
            selected_date = datetime(year, month, 1)

            if selected_date < start_date:
                return Response({'error': 'La fecha debe ser posterior al 1 de enero de 2013.'}, status=status.HTTP_400_BAD_REQUEST)

            # Construir la URL base
            url = f'https://www.sii.cl/valores_y_fechas/uf/uf{year}.htm'
            
            # Obtener todos los valores UF para el mes dado
            try:
                # Suponiendo que get_uf pueda recibir el día también
                uf_values = []
                for day in range(1, 32):
                    try:
                        # Verificar si el día es válido para el mes
                        datetime(year, month, day)
                        uf_value = get_uf(url, day, month)
                        uf_values.append({'date': f'{day:02d}/{month:02d}/{year}', 'uf_value': uf_value})
                    except ValueError:
                        # Día no válido para el mes
                        break
                return Response(uf_values)
            except RuntimeError as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
        except (ValueError, TypeError):
            return Response({'error': 'Los parámetros de fecha no son válidos.'}, status=status.HTTP_400_BAD_REQUEST)
