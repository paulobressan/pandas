import pandas as pd

# Criação de estruturas de dados, DataFrame e Series

# Series
# criando uma lista de dados
data = [1, 2, 3, 4, 5]
# Criando uma estrutra Series
s = pd.Series(data)
print(s)

# criando uma lista de index
index = ['Linha' + str(i) for i in range(5)]
# Criando uma estrutra Series com dados e index
s = pd.Series(data=data, index=index)
print(s)

# Podemos criar um dicionario e criar uma Series com data e index
data = {'Linha' + str(i): i+1 for i in range(5)}
# Não é necessario informar o index, porque o Pandas vai usar as keys do dicionario como as indexs
s = pd.Series(data)
print(s)

# Operações com Series
# Somar + 2 em todos registros da Serie
s1 = s + 2
print(s1)

# Somar duas Series, Se tiver valores de tipos difetens, vai ser atribuido como resultado o None
s2 = s + s1
print(s2)

# DATAFRAME
# Lista de Listas
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# criando DataFrame
df1 = pd.DataFrame(data=data)
print(df1)

# Criando lista de index de LINHAS para o dataFrame
index = ['Linha' + str(i) for i in range(3)]
df1 = pd.DataFrame(data=data, index=index)
print(df1)

# Criando uma lista de index de COLUNAS para o dataFrame
columns = ['Coluna' + str(i) for i in range(3)]
df1 = pd.DataFrame(data=data, index=index, columns=columns)
print(df1)

# Criando um DataFrame com base em um dicionario
data = {'Coluna0': {'Linha0': 1, 'Linha1': 4, 'Linha2': 7},
        'Coluna1': {'Linha0': 2, 'Linha1': 5, 'Linha2': 8},
        'Coluna2': {'Linha0': 3, 'Linha1': 6, 'Linha2': 9}}

df2 = pd.DataFrame(data)
print('DataFrame com dicionario\n', df2)


# Criando um DataFrame com base em uma lista de Tuplas
data = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
df3 = pd.DataFrame(data=data, index=index, columns=columns)
print('DataFrame com Tuplas\n', df3)

# Concatenar DataFrames

# Renomear todos os registros do DataFrame para 'A'
df1[df1 > 0] = 'A'
print(df1)

df2[df2 > 0] = 'B'
print(df2)

df3[df3 > 0] = 'C'
print(df3)

# Concatenar DataFrames com a função concat
# Um em cima ou outro
df4 = pd.concat([df1, df2, df3])
print(df4)

# O axis modifica o eixo em que vai ser feito a concatenação.
# Um do lado do outro
df4 = pd.concat([df1, df2, df3], axis=1)
print(df4)
