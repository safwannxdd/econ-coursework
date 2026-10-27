from pyexpat import model

print ("hello")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
df = pd.read_excel("Practical2.xlsx")
print(df.head())
print (df.describe())

df["race"] = df["race"].map({"white": 0, "black":1})
print(df.head())

df_reg = df[["lwage", "race"]].dropna()
X = sm.add_constant(df_reg["race"])   # adds the intercept term
y = df_reg["lwage"]

results = sm.OLS(y, X).fit()
print(results.summary())

pred = results.predict(X)
plt.scatter(df_reg["race"], df_reg["lwage"], alpha=0.4)
plt.plot(df_reg["race"], pred)  # line
plt.xticks([0, 1], ["White (0)", "Black (1)"])
plt.xlabel("Race")
plt.ylabel("lwage")
plt.title("Regression of lwage on race")
plt.show()

df["lwage"] = pd.to_numeric(df["lwage"], errors="coerce")
df["edu"]   = pd.to_numeric(df["edu"], errors="coerce")
df["exp"]   = pd.to_numeric(df["exp"], errors="coerce")
df_reg = df[["lwage", "race", "edu", "exp"]].dropna()
X = df_reg[["race", "edu", "exp"]]
X = sm.add_constant(X)

y = df_reg["lwage"]
result = sm.OLS(y, X).fit()
print(result.summary())

df["race_edu"] = df["race"] * df["edu"]
df["race_exp"] = df["race"] * df["exp"]
df_reg = df[["lwage", "race", "edu", "race_edu", "exp", "race_exp"]].dropna()
X = sm.add_constant(df_reg[["race", "edu", "race_edu", "exp", "race_exp"]])
y = df_reg["lwage"]

results = sm.OLS(y, X).fit()
print(results.summary())