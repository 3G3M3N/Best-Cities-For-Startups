import pandas as pd

df = pd.read_csv("Best Cities for Startups.csv")
df

df['country'] = df['country'].astype('str') 

df.loc[(df["country"]=="b' Turkey'")]

contries = df["country"]
contries.value_counts()

