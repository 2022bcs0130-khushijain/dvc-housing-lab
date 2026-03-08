import pandas as pd

df = pd.read_csv("data/housing.csv")
df_small = df.head(5000)
df_small.to_csv("data/housing.csv", index=False)

print("Version 1 dataset created:", df_small.shape)