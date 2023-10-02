import pandas as pd

df = pd.read_excel(r'C:\Users\rafae\OneDrive\Documentos\prog\coding\IB\data\renner_data.xlsx')
df = df.iloc[311:]

total_de_lojas = len(df)

contagem_por_regiao = df['Region'].value_counts()
contagem_por_regiao_df = contagem_por_regiao.reset_index()
contagem_por_regiao_df.columns = ['Region', 'Number of Stores']

tamanho_total_por_regiao = df.groupby('Region')['Total Area (m2)'].sum().reset_index(name='Tamanho Total (m²)')

tamanho_medio_por_regiao = df.groupby('Region')['Total Area (m2)'].mean().reset_index(name='Tamanho Médio (m²)').round(2)

tamanho_medio_no_brasil = df['Total Area (m2)'].mean().round(2)

lojas_por_regiao = df.groupby(['Region', 'Shopping Mall / Street']).size().unstack(fill_value=0).reset_index()
lojas_por_regiao['TOTAL'] = lojas_por_regiao['Shopping Mall'] + lojas_por_regiao['Street']
lojas_por_regiao['TOTAL %'] = (lojas_por_regiao['TOTAL']*100/total_de_lojas).round(1)

print(df)

print(contagem_por_regiao_df)

print("\nTamanho Total por Região:")
print(tamanho_total_por_regiao)

print("\nTamanho Médio por Região:")
print(tamanho_medio_por_regiao)

print("\nTamanho Médio no Brasil: ", tamanho_medio_no_brasil)

print("\nTotal de Lojas em Shopping no Brasil:", lojas_por_regiao['Shopping Mall'].sum())
print("Total de Lojas em Rua no Brasil:", lojas_por_regiao['Street'].sum())
print("Total de Lojas no Brasil:", total_de_lojas)

print("\nTotal de Lojas por Região:")
print(lojas_por_regiao)