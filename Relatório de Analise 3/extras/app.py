import pandas as pd

data = [[1,2,3], [4,5,6], [7,8,9]]

df = pd.DataFrame(data, list('321'), list('ZYX'))
print('DataFrame Original \n',df)

# Ordenando os index do DataFrame
df.sort_index(inplace = True)
print('Ordenando index \n',df)

# Ordenando pela coluna( ZYX = XYZ)
df.sort_index(inplace = True, axis=1)
print('Ordenando colunas \n',df)

# Ordenando os valores do eixo X
df.sort_values(by= 'X', inplace= True)
print('Ordenando valores do eixo X \n', df)

# Ordenando os valores do eixo Y
df.sort_values(by= '3', axis=1, inplace= True)
print('Ordenando valores do eixo Y \n', df)

