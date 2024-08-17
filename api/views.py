from rest_framework import viewsets
from rest_framework.response import Response
from datetime import datetime
from .utils.get_uf import get_uf

class UFViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            # Obtener los parámetros de la solicitud GET
            day = int(request.query_params.get('day', 0))
            month = int(request.query_params.get('month', 0))
            year = int(request.query_params.get('year', 0))

            # Validar los parámetros de fecha
            if not (1 <= day <= 31) or not (1 <= month <= 12):
                return Response({'error': 'El día o el mes no son válidos.'}, status=400)
            
            # Verificar que la fecha sea posterior al 1 de enero de 2013
            fecha_inicio = datetime(2013, 1, 1)
            fecha_ingresada = datetime(year, month, day)

            if fecha_ingresada >= fecha_inicio:
                # Construir la URL y obtener el valor de la UF
                url = f'https://www.sii.cl/valores_y_fechas/uf/uf{year}.htm'
                try:
                    uf_value = get_uf(url, day, month)
                    return Response({'uf_value': uf_value, 'date': fecha_ingresada.strftime('%d/%m/%Y')})
                except RuntimeError as e:
                    return Response({'error': str(e)}, status=500)
            return Response({'error': 'La fecha debe ser posterior al 1 de enero de 2013.'}, status=400)

        except (ValueError, TypeError):
            return Response({'error': 'Los parámetros de fecha no son válidos.'}, status=400)
