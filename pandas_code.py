import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

s = pd.Series([1, 3, 5, np.nan, 6, 8])

for i in range(100):
    print(i)

df = pd.DataFrame(np.random.randn(6, 4), columns=list("ABCD"))

df.describe()

df.loc[0,["A"]] = 100

df.mean(axis=1)

df["A"].value_counts()

df1 = df[0:2]
df2 = df[3:6]

pd.concat([df1,df2])

