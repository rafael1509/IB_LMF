import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderUnavailable
from time import sleep

# Carregue sua planilha Excel
planilha = pd.read_excel(r'C:\Users\rafae\OneDrive\Documentos\prog\coding\IB\data\c&a_data.xlsx')

# Inicialize o geocodificador
geolocator = Nominatim(user_agent="geoapiExercises")

# Função para obter coordenadas (latitude e longitude) a partir do endereço, cidade e estado
def get_coordinates(row):
    address = f"{row['Local']}, {row['Cidade']}, {row['Estado']}"
    try:
        location = geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude
        else:
            return None, None
    except (GeocoderTimedOut, GeocoderUnavailable):
        return None, None


# Adicione colunas de latitude e longitude à planilha
planilha['Latitude'], planilha['Longitude'] = zip(*planilha.apply(get_coordinates, axis=1))

# Salve a planilha atualizada
planilha.to_excel('sua_planilha_atualizada.xlsx', index=False)