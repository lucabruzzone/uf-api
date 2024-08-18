from functools import lru_cache
import requests
from bs4 import BeautifulSoup
from typing import Union

# LRU Cache para la función de obtener UF
@lru_cache(maxsize=100)
def get_uf(url: str, day: int, month: int) -> Union[str, None]:
    custom_header: dict[str, str] = {'user-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}
    try:
        # Agregar un tiempo de espera de 10 segundos
        res: requests.Response = requests.get(url, headers=custom_header, timeout=10)
        res.raise_for_status()  # Lanza un error si la solicitud falla
        soup: BeautifulSoup = BeautifulSoup(res.text, 'html.parser')
        table: BeautifulSoup = soup.find('table', id='table_export')
        table_body: BeautifulSoup = table.find('tbody')
        rows: list[BeautifulSoup] = table_body.find_all('tr')
        current_row: BeautifulSoup = rows[day - 1]
        months: list[BeautifulSoup] = current_row.find_all('td')
        correct_month: BeautifulSoup = months[month - 1]
        return correct_month.text.strip()
    
    # Manejo específico de errores de conexión
    except requests.exceptions.ConnectionError as e:
        raise RuntimeError(f"No se pudo establecer conexión con el servidor. Verifica tu conexión a Internet o la URL: {url}") from e
    
    # Manejo de otros errores de solicitudes
    except requests.exceptions.RequestException as e:
        # Re-lanzar la excepción original con información adicional
        raise RuntimeError(f"Error durante la solicitud a {url}: {e}") from e
