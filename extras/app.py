# EXTRA, IMPORTANDO DADOS

import pandas as pd

# importando json
json = open('./dados/aluguel.json')
df_json = pd.read_json(json)
print('JSON\n\n', df_json)

# importando txt, o sepadador do txt é tabulação
txt = open('./dados/aluguel.txt')
df_txt = pd.read_table(txt)
print('TXT \n\n', df_txt)

# importando xlsx(excel)
df_xlsx = pd.read_excel('./dados/aluguel.xlsx')
print('XLSX \n\n', df_xlsx)
