# ORGANIZANDO DATAFRAME

import pandas as pd

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
df = pd.DataFrame(data, list('321'), list('ZYX'))
print(df)
