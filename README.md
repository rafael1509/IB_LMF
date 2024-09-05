# Sobre
Essa é uma análise desenvolvida para o case do Núcleo de Investment Banking da FGV em uma parceria com o UBS BB. O objetivo era avaliar ganhos ou perdas em um possível M&A entre as varejistas Renner e C&A.

# Análise Geográfica das Lojas C&A e Renner

Este projeto tem como objetivo realizar uma análise geográfica das lojas da C&A e Renner, duas das principais redes varejistas do Brasil. O projeto está dividido em três principais etapas: coleta de coordenadas geográficas, análise de distâncias entre lojas e visualização das distribuições geográficas por meio de mapas.

## Coleta de Coordenadas Geográficas

A primeira etapa consiste em extrair as coordenadas (latitude e longitude) das lojas da C&A com base nos seus endereços. Utilizando a biblioteca `geopy`, conseguimos geocodificar os endereços e armazenar essas informações em um arquivo Excel, que serve como base para as análises subsequentes.
As informações sobre os endereços das lojas podem ser encontrados nos sites de RI das varejistas.

## Análise de Distâncias

Na segunda etapa, calculamos as distâncias entre as lojas da C&A e Renner para avaliar a proximidade entre as duas redes. Essa análise visa identificar possíveis oportunidades de otimização de custos de transporte, considerando lojas que estejam geograficamente próximas.

## Visualização com Mapas

Por fim, criamos mapas dois mapas para visualizar a distribuição geográfica das lojas de ambas as redes: um de calor e outro com marcadores. Para isso utilizamos a biblioteca `folium`. Estes mapas interativos permitem uma melhor compreensão da concentração de lojas em diferentes regiões do Brasil, facilitando a identificação de padrões e possíveis áreas de interesse.

## Conclusão
A proximidade geográfica entre as lojas da C&A e Renner sugere que há potencial para ganhos de sinergia, especialmente na otimização dos custos de transporte entre os centros de distribuição e os pontos de venda. A análise dos mapas revelou diferenças significativas na distribuição regional das lojas: enquanto a C&A tem uma presença forte no Nordeste, a Renner se destaca no Sul do Brasil (ambas tem atuação relevante no Sudeste). Essas distinções regionais podem indicar estratégias de mercado diferentes, refletindo as particularidades demográficas e econômicas de cada região.
