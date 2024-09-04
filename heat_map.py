'''
conseguir avaliar distribuição geográfica das lojas por meio de um heatmap
'''

import pandas as pd
import folium
from folium.plugins import HeatMap

c_df = pd.read_excel(r'C:\Users\rafae\OneDrive\Documentos\prog\coding\IB_organized\output\c&a_coord.xlsx')
r_df = pd.read_excel(r'C:\Users\rafae\OneDrive\Documentos\prog\coding\IB_organized\output\renner_coord.xlsx')
r_df = r_df[r_df['Business'] == 'Renner']

# Criar um mapa
r_brasil_map = folium.Map(location=[-14.235, -51.925], zoom_start=4)
c_brasil_map = folium.Map(location=[-14.235, -51.925], zoom_start=4)

# Criar uma lista de coordenadas para o mapa de calor
r_heat_data = r_df[['Latitude', 'Longitude']].values.tolist()
c_heat_data = c_df[['Latitude', 'Longitude']].values.tolist()

gradient = {
    0.0: 'blue',
    0.2: 'lightblue',
    0.3: 'lightgreen',
    0.4: 'yellow',
    
    0.5: 'gold',
    0.6: 'orange',
    0.7: 'darkorange',
    0.8: 'red',
    0.9: 'darkred',
    1.0: 'maroon'
}

# Mapa de calor com a paleta personalizada
HeatMap(r_heat_data, gradient=gradient).add_to(r_brasil_map)
HeatMap(c_heat_data, gradient=gradient).add_to(c_brasil_map)

# Salvar o mapa de calor em um arquivo HTML
r_brasil_map.save("output/renner_heat_map_lojas.html")
c_brasil_map.save("output/c&a_heat_map_lojas.html")
