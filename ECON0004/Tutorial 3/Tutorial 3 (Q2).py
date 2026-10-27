import pandas as pd
import statsmodels.api as sm

df_wage = pd.read_excel("Tutorial 3 dataset 0.xlsx")
print(df_wage.head())

x = df_wage[["educ"]]
y = df_wage[["lnwage"]]

X = sm.add_constant(x)

model = sm.OLS(y, X).fit()
print(model.summary())

x = df_wage[["educ","exp"]]
y = df_wage[["lnwage"]]
X = sm.add_constant(x)

model1 = sm.OLS("lnwage ~ educ", data=df_wage).fit()

