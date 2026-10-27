import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import pingouin as pg
from lets_plot import *
from numpy import array
import statsmodels.api as sm
from statsmodels.iolib.summary2 import summary_col

df = pd.read_csv("/Users/muhammadsafwan/PyCharmMiscProject/ECON0004/Python Empirical Project/Applied Empirical Project(Sheet1) (2).csv")

# Keep only needed columns
cols = ['Gini', 'EduSpend','LnGDPPC', 'GDPPC', 'GOVSpend', 'Unem', 'Urban']
df = df[cols].copy()

# Convert all columns to numeric
for col in cols:
    df[col] = (
        df[col]
        .astype(str)                           # make everything string first
        .str.replace(',', '', regex=False)    # remove commas
        .str.replace('%', '', regex=False)    # remove percent signs
        .str.strip()                          # remove spaces
    )
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Drop rows with missing values in regression variables
df = df.dropna(subset=cols)

# Create squared term
df['EduSpend_sq'] = df['EduSpend'] ** 2

# Define variables
y = df['Gini']
X = df[['EduSpend', 'EduSpend_sq', 'LnGDPPC', 'GOVSpend', 'Unem', 'Urban']]

# =========================
# 2. Run regressions
# =========================
y = df['Gini']

# Column (1): full model
X1 = df[['EduSpend', 'LnGDPPC', 'Unem', 'Urban']]
X1 = sm.add_constant(X1)
m1 = sm.OLS(y, X1).fit()

# Column (2): omit Urban
X2 = df[['EduSpend', 'EduSpend_sq', 'LnGDPPC', 'Unem', 'Urban']]
X2 = sm.add_constant(X2)
m2 = sm.OLS(y, X2).fit()

plt.show()
print(m2.summary())
print(m1.summary())

# 3. Scatter plots
edu_range = np.linspace(df['EduSpend'].min(), df['EduSpend'].max(), 200)

lngdppc_mean = df['LnGDPPC'].mean()
unem_mean = df['Unem'].mean()
urban_mean = df['Urban'].mean()

# Model 1 predictions
X1_plot = pd.DataFrame({
    'const': 1,
    'EduSpend': edu_range,
    'LnGDPPC': lngdppc_mean,
    'Unem': unem_mean,
    'Urban': urban_mean
})
y1_plot = m1.predict(X1_plot)

plt.figure(figsize=(8, 6))
plt.scatter(df['EduSpend'], df['Gini'], alpha=0.7)
plt.plot(edu_range, y1_plot)
plt.xlabel('Education spending (%)')
plt.ylabel('Gini coefficient')
plt.title('Model 1: Linear relationship')
plt.grid(True)
plt.show()

# Model 2 predictions
X2_plot = pd.DataFrame({
    'const': 1,
    'EduSpend': edu_range,
    'EduSpend_sq': edu_range**2,
    'LnGDPPC': lngdppc_mean,
    'Unem': unem_mean,
    'Urban': urban_mean
})
y2_plot = m2.predict(X2_plot)

plt.figure(figsize=(8, 6))
plt.scatter(df['EduSpend'], df['Gini'], alpha=0.7)
plt.plot(edu_range, y2_plot)
plt.xlabel('Education spending (%)')
plt.ylabel('Gini coefficient')
plt.title('Model 2: Quadratic relationship')
plt.grid(True)
plt.show()

beta_1 = 0.0436
beta_2 = -0.0064

print("dGini/dEduSpend = beta_1 + 2*beta_2*EduSpend")
print(f"dGini/dEduSpend = {beta_1} + 2({beta_2})EduSpend")

a = 2 * beta_2
print(f"So: {beta_1} {a:+.4f}EduSpend = 0")

turning_point = -beta_1 / a

print(f"EduSpend = {-beta_1} / {a}")
print(f"EduSpend ≈ {turning_point:.2f}%")