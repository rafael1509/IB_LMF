'''
conseguir avaliar distribuição geográfica das lojas por meio de marcadores
'''

import pandas as pd
import folium

c_df = pd.read_excel(r'C:\Users\rafae\OneDrive\Documentos\prog\coding\IB_organized\output\c&a_coord.xlsx')
r_df = pd.read_excel(r'C:\Users\rafae\OneDrive\Documentos\prog\coding\IB_organized\output\renner_coord.xlsx')
r_df = r_df[r_df['Business'] == 'Renner']

# Criar um mapa
r_brasil_map = folium.Map(location=[-14.235, -51.925], zoom_start=4)
c_brasil_map = folium.Map(location=[-14.235, -51.925], zoom_start=4)
combined_brasil_map = folium.Map(location=[-14.235, -51.925], zoom_start=4)

# Adicionar marcadores ao mapa para Renner
for index, row in r_df.iterrows():
    folium.Marker(location=[row['Latitude'], row['Longitude']],
                  icon=folium.Icon(color='red', prefix=''), shadow=None).add_to(r_brasil_map)
    folium.Marker(location=[row['Latitude'], row['Longitude']],
                  icon=folium.Icon(color='red', prefix=''), shadow=None).add_to(combined_brasil_map)

# Adicionar marcadores ao mapa para C&A
for index, row in c_df.iterrows():
    folium.Marker(location=[row['Latitude'], row['Longitude']],
                  icon=folium.Icon(color='blue', prefix=''), shadow=None).add_to(c_brasil_map)
    folium.Marker(location=[row['Latitude'], row['Longitude']],
                  icon=folium.Icon(color='blue', prefix=''), shadow=None).add_to(combined_brasil_map)

# Salvar o mapa com marcadores em um arquivo HTML
r_brasil_map.save("output/renner_marker_map_lojas.html")
c_brasil_map.save("output/c&a_marker_map_lojas.html")
combined_brasil_map.save("output/combined_marker_map_lojas.html")
