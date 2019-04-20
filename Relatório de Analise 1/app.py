# RELATÓRIO DE ANALISE 1

# Importando pandas e atribuindo um alias a ele
import pandas as pd

# Importando os dados de um csv
# sep = separador, por default é ",", e o arquivo é ";", então podemos atribuir o separador
# O retorno da função read_csv é um objeto do tipo DataFrame.
# Ele é parecido com uma planilha de excel, ele temo linhas, colunas e titulos
dados = pd.read_csv("dados/aluguel.csv", sep=";")

# Exibir informações sobre os dados carregados
# print(dados.info())

# Exibir somente 10 linhas
print(dados.head(10))

# INFORMAÇÕES GERAIS SOBRE A BASE DE DADOS
# Visualizar os tipos de cada coluna
print(dados.dtypes)

# Criando um DataFrame com os tipos de dados do DataFrame importado. Vamos definir o nome da coluna(dtype) de Tipos de Dados
tipos_de_dados = pd.DataFrame(dados.dtypes, columns=['Tipos de Dados'])
# Adicionando um nome para a coluna de variaveis(Titulo de cada coluna do DataFrame importado)
tipos_de_dados.columns.name = 'Variáveis'
print(tipos_de_dados)

# Tamanho da dimenção do array
print(dados.shape)
# (32960, 9) = (linhas, variaveis ou colunas)

print(f"A base de dados apresenta {dados.shape[0]} registros(imóveis) e {dados.shape[1]} variaveis (colunas)")
