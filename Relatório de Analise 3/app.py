# Relatório de Analise II

import pandas as pd

# Imóveis Residenciais
dados = pd.read_csv('../dados/aluguel.csv', sep=';')

# Criando uma lista somente com os tipos de imoveis
list(dados['Tipo'].drop_duplicates())
residencial = ['Quitinete', 'Casa', 'Apartamento',
               'Casa de Condomínio', 'Casa de Vila']

# A isin define true para os Tipos que estiver na lista de residencial
selecao = dados['Tipo'].isin(residencial)
# Quando passamos um array de true e false com o mesmo tamanho de indece do DataFrame, o pandas mantem somente o True e remove os false.
# Com isso podemos filtrar somente os dados de imoveis que tem algum dos tipos de residencial
dados_residencial = dados[selecao]
# Para confirmar se foi filtrados os itens corretos, podemos selecionar somente os tipos removendo todos duplicados
print(dados_residencial['Tipo'].drop_duplicates())

# Reconstruir o index para organizar as lacunas deixada pelo filtro
dados_residencial.index = range(dados_residencial.shape[0])
print(dados_residencial)

# EXPORTANDO A BASE DE DADOS
# Para exportar, informamos o caminho junto o nome e a extenção do arquivo.
# O separador do csv, por default é a virgula e index=False para ele não exportar o index.
dados_residencial.to_csv('../dados/aluguel_residencial.csv', sep=';', index=False)

dados_residencial_2 = pd.read_csv('../dados/aluguel_residencial.csv', sep=';')
print(dados_residencial_2)
