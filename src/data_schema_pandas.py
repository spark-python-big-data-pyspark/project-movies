import pandas as pd

# Leer datos
df_name = pd.read_csv("../data/name.tsv", sep="\t")

# Mostrar esquema
print(df_name.dtypes)