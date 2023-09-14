import pandas as pd

df = pd.read_csv("data.csv")

df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

#renomear colunas
df.rename(columns={'OldName1':'Newname1', 'OldName2':'Newname2'}, inplace=True)

#remover colunas desnecessárias
df.drop(columns=['UnneededColumn1', 'UnneededColumn2'], inplace=True)
print(df)

# subsitutir valores nao numericas
df['NumericColumn']= df['NumericColumn'].replace('[^0-9.]', '', regex=True).astype(float)

# criar uma nova coluna
df['Novacoluna'] = df['Column1'] + df['Column2']
print(df)