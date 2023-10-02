import pandas as pd
import folium
from geopy.geocoders import Nominatim
from folium.plugins import HeatMap

r_estados = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO']
r_cidades_por_estado = [['RIO BRANCO'], ['ARAPIRACA', 'MACEIÓ'], ['MANAUS'], ['MACAPÁ'], ['CAMAÇARI', 'FEIRA DE SANTANA', 'ITABUNA', 'JUAZEIRO', 'LAURO DE FREITAS', 'SALVADOR', 'TEIXEIRA DE FREITAS', 'VITÓRIA DA CONQUISTA'], ['EUSÉBIO', 'FORTALEZA', 'JUAZEIRO DO NORTE', 'SOBRAL'], ['BRASÍLIA'], ['CACHOEIRO DO ITAPEMIRIM', 'CARIACICA', 'LINHARES', 'SERRA', 'VILA VELHA', 'VITÓRIA'], ['ANÁPOLIS', 'APARECIDA DE GOIÂNIA', 'CATALÃO', 'GOIÂNIA', 'JATAÍ', 'RIO VERDE', 'VALPARAÍSO DE GOIÁS'], ['IMPERATRIZ', 'SÃO JOSÉ DO RIBAMAR', 'SÃO LUÍS'], ['ALFENAS', 'BELO HORIZONTE', 'BETIM', 'BARBACENA', 'CONTAGEM', 'DIVINÓPOLIS', 'GOVERNADOR VALADARES', 'IPATINGA', 'JUIZ DE FORA', 'MONTES CLAROS', 'MURIAÉ', 'POUSO ALEGRE', 'POÇOS DE CALDAS', 'SETE LAGOAS', 'UBERABA', 'UBERLÂNDIA', 'VARGINHA'], ['CAMPO GRANDE', 'DOURADOS', 'TRÊS LAGOAS'], ['CUIABÁ', 'RONDONÓPOLIS', 'SINOP', 'SORRISO', 'TANGARÁ DA SERRA', 'VÁRZEA GRANDE'], ['ANANINDEUA', 'BELÉM', 'MARABÁ', 'PARAUAPEBAS', 'SANTARÉM'], ['CAMPINA GRANDE', 'JOÃO PESSOA'], ['CAMARAGIBE', 'CARUARU', 'JABOATÃO DOS GUARARAPES', 'OLINDA', 'PAULISTA', 'RECIFE'], ['PARNAÍBA', 'TERESINA'], ['CASCAVEL', 'CAMPO MOURÃO', 'CURITIBA', 'FOZ DO IGUAÇU', 'GUARAPUAVA', 'LONDRINA', 'MARINGÁ', 'PARANAVAÍ', 'PONTA GROSSA', 'PATO BRANCO', 'SÃO JOSÉ DOS PINHAIS', 'UMUARAMA'], ['ANGRA DOS REIS', 'CAMPOS DOS GOYTACAZES', 'DUQUE DE CAXIAS', 'ITABORAÍ', 'MACAÉ', 'MARICÁ', 'NITERÓI', 'NOVA FRIBURGO', 'NOVA IGUAÇU', 'PETROPOLIS', 'RESENDE', 'RIO DE JANEIRO', 'SÃO GONÇALO', 'SÃO JOÃO DE MERITI', 'TERESÓPOLIS', 'VOLTA REDONDA'], ['MOSSORÓ', 'NATAL'], ['CACOAL', 'PORTO VELHO'], ['BOA VISTA'], ['ALEGRETE', 'BAGÉ', 'BENTO GONÇALVES', 'CACHOEIRA DO SUL', 'CACHOEIRINHA', 'CANOAS', 'CAPÃO DA CANOA', 'CAXIAS DO SUL', 'CANELA', 'CARAZINHO', 'CRUZ ALTA', 'ERECHIM', 'ESTEIO', 'FARROUPILHA', 'GARIBALDI', 'GRAMADO', 'GRAVATAÍ', 'GUAÍBA', 'IJUÍ', 'LAJEADO', 'NOVO HAMBURGO', 'PASSO FUNDO', 'PELOTAS', 'PORTO ALEGRE', 'RIO GRANDE', 'SANTA CRUZ DO SUL', 'SANTA MARIA', 'SANTA ROSA', 'SANTO ÂNGELO', 'SAPUCAIA', 'SÃO LEOPOLDO', 'TORRES', 'TRAMANDAÍ', 'TAQUARA', 'URUGUAIANA'], ['BALNEÁRIO CAMBORIÚ', 'BLUMENAU', 'CHAPECÓ', 'CRICIÚMA', 'FLORIANÓPOLIS', 'ITAJAÍ', 'JARAGUÁ DO SUL', 'JOINVILLE', 'LAGES', 'PALHOÇA', 'RIO DO SUL', 'SÃO BENTO DO SUL', 'SÃO JOSÉ', 'TUBARÃO'], ['ARACAJU'], ['ARARAQUARA', 'ARARAS', 'ARAÇATUBA', 'ASSIS', 'BARRETOS', 'BARUERI', 'BAURU', 'BOTUCATU', 'BRAGANÇA PAULISTA', 'CAMPINAS', 'CARAGUATATUBA', 'COTIA', 'CAJAMAR', 'CATANDUVA', 'DIADEMA', 'FRANCA', 'GUARATINGUETÁ', 'GUARUJÁ', 'GUARULHOS', 'INDAIATUBA', 'ITAPETININGA', 'ITAQUAQUECETUBA', 'ITU', 'JACAREÍ', 'JAÚ', 'JUNDIAÍ', 'LIMEIRA', 'LORENA', 'MARÍLIA', 'MAUÁ', 'MOGI DAS CRUZES', 'MOGI GUAÇU', 'OSASCO', 'OURINHOS', 'PINDAMONHANGABA', 'PIRACICABA', 'PRAIA GRANDE', 'PRESIDENTE PRUDENTE', 'PENÁPOLIS', 'RIBEIRÃO PRETO', 'RIO CLARO', "SANTA BÁRBARA D'OESTE",'SANTO ANDRÉ', 'SANTOS', 'SOROCABA', 'SUMARÉ', 'SUZANO', 'SÃO BERNARDO DO CAMPO', 'SÃO CAETANO DO SUL', 'SÃO CARLOS', 'SÃO JOSÉ DO RIO PRETO', 'SÃO JOSÉ DOS CAMPOS', 'SÃO PAULO', 'SÃO VICENTE', 'TABOÃO DA SERRA', 'TAUBATÉ', 'VALINHOS', 'VOTORANTIM'], ['PALMAS']]
r_numero_lojas_por_cidade = [[1], [1, 3], [6], [1], [1, 1, 1, 1, 1, 7, 1, 2], [2, 8, 1, 1], [10], [1, 1, 1, 2, 3, 1], [1, 1, 1, 6, 1, 1, 1], [1, 1, 4], [4, 8, 2, 2, 2, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 2, 1], [3, 1, 1], [2, 1, 1, 1, 1, 1], [1, 5, 1, 1, 1], [1, 2], [1, 1, 1, 1, 1, 6], [1, 3], [1, 9, 1, 2, 1, 3, 2, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 26, 1, 1, 1, 2], [1, 3], [1, 1], [2], [1, 1, 1, 1, 1, 3, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 14, 2, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1], [1, 2, 1, 1, 5, 1, 1, 2, 1, 1, 1, 1, 2, 1], [3], [1, 1, 1, 1, 1, 3, 2, 1, 1, 6, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 4, 1, 1, 2, 2, 2, 1, 1, 3, 1, 1, 3, 3, 40, 1, 1, 2, 1, 2], [1]]

# Criar um DataFrame a partir dos dados
r_data = []

# renner
for i in range(len(r_estados)):
    r_estado = r_estados[i]
    r_cidades = r_cidades_por_estado[i]
    r_num_lojas = r_numero_lojas_por_cidade[i]
    
    for j in range(len(r_cidades)):
        r_cidade = r_cidades[j]
        r_num_lojas_cidade = r_num_lojas[j]
        r_data.append([r_cidade, r_estado, r_num_lojas_cidade])        

r_df = pd.DataFrame(r_data, columns=['Cidade', 'Estado', 'Número de Lojas'])
c_df = pd.read_excel(r'C:\Users\rafae\OneDrive\Documentos\prog\coding\IB\data\c&a_data_coord.xlsx')

# Inicializar o objeto geocoder
geolocator = Nominatim(user_agent="geoapiExercises")

# Função para obter as coordenadas de uma cidade
def get_lat_long(city, state):
    location = geolocator.geocode(f"{city}, {state}, Brazil")
    if location:
        return (location.latitude, location.longitude)
    else:
        return (None, None)

# Adicionar colunas de latitude e longitude ao DataFrame (c&a ja tem)
r_df['Latitude'], r_df['Longitude'] = zip(*r_df.apply(lambda row: get_lat_long(row['Cidade'], row['Estado']), axis=1))

# Criar um mapa
r_brasil_map = folium.Map(location=[-14.235, -51.925], zoom_start=4)
c_brasil_map = folium.Map(location=[-14.235, -51.925], zoom_start=4)

# Criar uma lista de coordenadas para o mapa de calor
r_heat_data = r_df[['Latitude', 'Longitude', 'Número de Lojas']].values.tolist()
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
r_brasil_map.save("renner_heat_map_lojas.html")
c_brasil_map.save("c&a_heat_map_lojas.html")