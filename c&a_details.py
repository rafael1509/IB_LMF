import pandas as pd

correspondencia_estado_regiao = {
    'AC': 'Norte',
    'AL': 'Nordeste',
    'AM': 'Norte',
    'AP': 'Norte',
    'BA': 'Nordeste',
    'CE': 'Nordeste',
    'DF': 'Centro-Oeste',
    'ES': 'Sudeste',
    'GO': 'Centro-Oeste',
    'MA': 'Nordeste',
    'MG': 'Sudeste',
    'MS': 'Centro-Oeste',
    'MT': 'Centro-Oeste',
    'PA': 'Norte',
    'PB': 'Nordeste',
    'PE': 'Nordeste',
    'PI': 'Nordeste',
    'PR': 'Sul',
    'RJ': 'Sudeste',
    'RN': 'Nordeste',
    'RO': 'Norte',
    'RR': 'Norte',
    'RS': 'Sul',
    'SC': 'Sul',
    'SE': 'Nordeste',
    'SP': 'Sudeste',
    'TO': 'Norte'
}

df = pd.read_excel(r'C:\Users\rafae\OneDrive\Documentos\prog\coding\IB\data\c&a_data_coord.xlsx')

# Criar uma nova coluna 'Regiao' no DataFrame com base na correspondência de estados e regiões
df['Regiao'] = df['Estado'].map(correspondencia_estado_regiao)

total_de_lojas = len(df)
contagem_lojas_por_regiao = df.groupby('Regiao').size().reset_index(name='Número de Lojas')
tamanho_total_por_regiao = df.groupby('Regiao')['Salão de Vendas - m²'].sum().reset_index(name='Tamanho Total (m²)')
tamanho_medio_por_regiao = df.groupby('Regiao')['Salão de Vendas - m²'].mean().reset_index(name='Tamanho Médio (m²)').round(2)
lojas_por_regiao = df.groupby(['Regiao', 'SHOPPING/STREET']).size().unstack(fill_value=0).reset_index()
lojas_por_regiao['TOTAL'] = lojas_por_regiao['SHOPPING MALL'] + lojas_por_regiao['STREET']
lojas_por_regiao['TOTAL %'] = (lojas_por_regiao['TOTAL']*100/total_de_lojas).round(1)
tamanho_medio_no_brasil = df['Salão de Vendas - m²'].mean().round(2)


# Imprimir os resultados
print(df)

print("Tamanho Total por Região:")
print(tamanho_total_por_regiao)

print("\nTamanho Médio por Região:")
print(tamanho_medio_por_regiao)

print("\nTamanho Médio no Brasil: ", tamanho_medio_no_brasil)

print("\nTotal de Lojas em Shopping no Brasil:", lojas_por_regiao['SHOPPING MALL'].sum())
print("Total de Lojas em Rua no Brasil:", lojas_por_regiao['STREET'].sum())
print("Total de Lojas no Brasil:", total_de_lojas)

print("\nTotal de Lojas por Região:")
print(lojas_por_regiao)

df.to_excel('c&a_graficos.xlsx', index=False)

