'''
Objetivo é conseguir as coordenadas de cada loja da C&A
'''

import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderUnavailable
from time import sleep

# Carregue sua planilha Excel
planilha = pd.read_excel(r'C:\Users\rafae\OneDrive\Documentos\prog\coding\IB_organized\data\c&a_data.xlsx')

# Inicialize o geocodificador
geolocator = Nominatim(user_agent="geocode_app")

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


# Adicionando colunas de latitude e longitude à planilha
planilha['Latitude'], planilha['Longitude'] = zip(*planilha.apply(get_coordinates, axis=1))

# Salvando
# obs: o geopy nao consegue achar a localização exata de todas as lojas, então tive que
# ajeitar alguns detalhes manualmente
planilha.to_excel('output/c&a_coord.xlsx', index=False)
