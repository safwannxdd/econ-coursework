import pandas as pd

df_temp = pd.read_excel("Tutorial 2 dataset.xlslx", skiprows=1, na_values"***",)





df_co2 = pd.read_excel("Tutorial 3 CO2 dataset.xlsx")
print(df_co2.head())

df_co2_july = df_co2.loc[df_co2["Month"] == 7]
print(df_co2_july.head())

#Have to do 1.2 first to get "df" information
df_temp_co2 = pd.merge(df_co2_july, df, on="Year")
print(df_temp_co2[["Year", "July", "Trend"]].head())

