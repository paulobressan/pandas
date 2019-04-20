# Relatório de Analise II

import pandas as pd

# Tipos de Imóveis
# Importando dados do csv
dados = pd.read_csv('../dados/aluguel.csv', sep=';')
# Acessando uma variavel especifica
# print(dados['Tipo'])

# Ao selecionar uma coluna especifica, o retorno é do tipo Series
# O Series é um array unedimensional, ela tem uma coluna.
# Um DataFrame é uma lista de Series
tipo_de_imovel = dados['Tipo']
# print('Tipo de uma coluna de dados', type(tipo_de_imovel))

# Remover os itens duplicados. A função pega o primeiro item e remove o restante duplicado.
# Inplace = Altera o valor da variavel tipo_de_imovel
# não sendo necessario atribuir o retorno de drop_duplicates em uma variavel
tipo_de_imovel.drop_duplicates(inplace=True)
# print(tipo_de_imovel)

##ORGANIZANDO A VISIALIZAÇÃO

# Criando um dataframe com base nos dados tipo_de_imovel
tipo_de_imovel = pd.DataFrame(tipo_de_imovel)
# Ao remover os duplicados, o index esta com intervalos, vamos numerar corretamente
tipo_de_imovel.index = range(tipo_de_imovel.shape[0])
# Adicionando um nome a coluna de index
tipo_de_imovel.columns.name = 'Id'
print(tipo_de_imovel)