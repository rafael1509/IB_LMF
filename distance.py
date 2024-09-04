'''
analisar distância entre as lojas das varejistas para avaliar possível
ganhos com redução de custo de transporte
'''

from geopy.distance import geodesic
import pandas as pd

c_df = pd.read_excel(r'C:\Users\rafae\OneDrive\Documentos\prog\coding\IB_organized\output\c&a_coord.xlsx')
r_df = pd.read_excel(r'C:\Users\rafae\OneDrive\Documentos\prog\coding\IB_organized\output\renner_coord.xlsx')
r_df = r_df[r_df['Business'] == 'Renner']

def calcular_distancia(coord1, coord2):
    return geodesic(coord1, coord2).kilometers

distancias = []

# Iterar sobre as linhas do dataframe da Renner
for _, renner_loja in r_df.iterrows():
    renner_coord = (renner_loja['Latitude'], renner_loja['Longitude'])
    
    # Calcular a distância para cada loja da C&A
    c_df['Distancia'] = c_df.apply(lambda row: calcular_distancia(renner_coord, (row['Latitude'], row['Longitude'])), axis=1)
    
    distancias.append(min(c_df['Distancia']))

# "histograma"
intervalos = [0, 0, 0, 0, 0, 0, 0]
for i, distancia in enumerate(distancias):
    if distancia < 0.5:
        intervalos[0] += 1
    elif distancia < 2:
        intervalos[1] += 1
    elif distancia < 4:
        intervalos[2] += 1   
    elif distancia < 6:
        intervalos[3] += 1 
    elif distancia < 10:
        intervalos[4] += 1  
    elif distancia < 20:
        intervalos[5] += 1  
    else:
        intervalos[6] += 1 

print(f"{intervalos[0]} lojas da renner com distância até 0.5 km da loja da C&A mais próxima")
print(f"{intervalos[1]} lojas da renner com distância até 2 km da loja da C&A mais próxima")
print(f"{intervalos[2]} lojas da renner com distância até 4 km da loja da C&A mais próxima")
print(f"{intervalos[3]} lojas da renner com distância até 6 km da loja da C&A mais próxima")
print(f"{intervalos[4]} lojas da renner com distância até 10 km da loja da C&A mais próxima")
print(f"{intervalos[5]} lojas da renner com distância até 20 km da loja da C&A mais próxima")
print(f"{intervalos[6]} lojas da renner com distância maior que 20 km da loja da C&A mais próxima")
