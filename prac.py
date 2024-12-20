import pandas as pd
import numpy as np
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Ella"],
    "Age": [25, 30, 35, 40, 45],
    "Score": [85, 90, 95, 80, 75]
}
df=pd.DataFrame(data)
# print(df)
# print(df.index.tolist())
# print(df.columns)
# print(df.head())
# print(df.tail())
# print(df.describe())
# des=df.describe()
# print(des.index.tolist())
# print(df.info())
print(df.size)  #15
coffee2=pd.read_csv("https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/warmup-data/coffee.csv")
# print(coffee2)
# print(np.zeros(5))
print(np.arange(20,10,-2))

