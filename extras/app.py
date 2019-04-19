# EXTRA, IMPORTANDO DADOS
import pandas as pd
# Utilizado para importar e manipular arquivos xlsx(excel)
import xlrd
# Utilizado para importar e manipular arquivos HTML
import lxml

# importando json
json = open('./dados/aluguel.json')
df_json = pd.read_json(json)
print('JSON\n\n', df_json)

# importando txt, o sepadador do txt é tabulação
txt = open('./dados/aluguel.txt')
df_txt = pd.read_table(txt)
print('TXT \n\n', df_txt)

# importando xlsx(excel), Para importar o arquivo, temos que utilizar o pacote xlrd.(import xlrd)
df_xlsx = pd.read_excel('./dados/aluguel.xlsx')
print('XLSX \n\n', df_xlsx)

# Importando uma tabela de uma pagina html
df_html = pd.read_html('./dados/dados_html_1.html')
# Ou podemos importar diretamento do arquivo retornado pelo servidor
df_html = pd.read_html(
    'https://unafiscosaude.org.br/site/tabelas-de-precos-dos-planos-ativos-para-comercializacao/')
print(df_html[0])

# Em uma pagina html onde temos mais de uma tabela,é retornado uma lista de dataFrame
df_html2 = pd.read_html(
    'https://www.federalreserve.gov/releases/h3/current/default.htm')
print(len(df_html2))
print('tabela 1', df_html2[0])
print('tabela 2', df_html2[1])
print('tabela 3', df_html2[2])
