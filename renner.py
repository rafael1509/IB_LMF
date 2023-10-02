from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from time import sleep

navegador = webdriver.Chrome()
navegador.get('https://www.lojasrenner.com.br/nossas-lojas')

# criar lista com nome dos estados
estado_select = navegador.find_element('id', 'stateLocationStore')
select_estado = Select(estado_select)
estados = select_estado.options
nomes_estados = [estado.text for estado in estados]
del nomes_estados[0]

cidades_por_estado = []
numero_lojas = []
numero_lojas_por_estado = []

print(nomes_estados)

for estado in nomes_estados:
    select_estado.select_by_visible_text(estado)

    # Espera até que o elemento select para a cidade seja visível
    wait = WebDriverWait(navegador, 10)
    sleep(1)

    # Criar lista com nome das cidades
    cidade_select = navegador.find_element('id', 'cityLocationStore')
    select_cidade = Select(cidade_select)
    opcoes_cidades = select_cidade.options
    nomes_cidades = [cidade.text for cidade in opcoes_cidades]
    cidades_por_estado.append(nomes_cidades)
    del nomes_cidades[0]
    sleep(0.25)

    for cidade in nomes_cidades:
        try:
            select_cidade.select_by_visible_text(cidade)
        except NoSuchElementException:
            if cidade == 'LAURO DE FREITAS':
                select_cidade.select_by_visible_text('Lauro de Freitas')
            if cidade == 'TEIXEIRA DE FREITAS':
                select_cidade.select_by_visible_text('Teixeira de Freitas')

        wait = WebDriverWait(navegador, 10)
        sleep(0.25)

        lojas = navegador.find_elements('css selector', '.row_result')

        # Obtém o número de lojas
        numero_lojas_por_cidade = len(lojas)

        numero_lojas.append(numero_lojas_por_cidade)
    
    numero_lojas_por_estado.append(numero_lojas)
    numero_lojas = []

# tirar duplicações
# cidades_por_estado = [list(set(cidades)) for cidades in cidades_por_estado]
print(cidades_por_estado)
print(numero_lojas_por_estado)

# Fecha o navegador
navegador.quit()
