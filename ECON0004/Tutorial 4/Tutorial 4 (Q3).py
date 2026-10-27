import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import pingouin as pg
from lets_plot import *
from numpy import array

LetsPlot.setup_html(no_js=True)

path_to_data = Path("Dataset Project 3.xlsx")
df = pd.read_excel(path_to_data)
var_info = pd.read_excel(path_to_data, sheet_name=  "Data Dictionary")
data = pd.read_excel(path_to_data, sheet_name = "Data")
data.info()

for col in ["type", "taxed", "supp", "store_id", "store_type", "type2", "product_id"]:
    data[col] = data[col].astype("category")

# rename some of the categories
data["taxed"] = data["taxed"].cat.rename_categories(["not taxed", "taxed"])
data["supp"] = data["supp"].cat.rename_categories(["standard", "supplemental"])
data["store_type"] = data["store_type"].cat.rename_categories(
    ["Large supermarket", "Small supermarket", "Pharmacy", "Gas station"]
)

data["time"].unique()
array(['DEC2014', 'JUN2015', 'MAR2015'], dtype=object)

data.loc[data["time"] == "MAR2015", "time"] = "MAR2016"
data["time"] = data["time"].astype("category")
no_stores = len(data["store_id"].unique())
no_products = len(data["product_id"].unique())
print(f"The {no_stores=} while the {no_products=}.")


pd.crosstab(index=data["store_type"], columns=[data["time"], data["taxed"]], margins=True)
print (pd.crosstab(index=data["store_type"], columns=[data["time"], data["taxed"]]))

pd.crosstab(index=data["type"], columns=data["time"], margins=True)
print (pd.crosstab(index=data["type"], columns=data["time"], margins=True))

pd.crosstab(index=data["store_type"], columns=data["time"])
print (pd.crosstab(index=data["store_type"], columns=data["time"]))