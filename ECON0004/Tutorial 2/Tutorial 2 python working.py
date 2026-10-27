import pandas as pd
import numpy as np
import lets_plot as lplt
import matplotlib as mpl
import matplotlib.pyplot as plt
df = pd.read_csv ("Tutorial 2 dataset.csv",skiprows=1,na_values="***",)


df = df.set_index("Year")
df.head ()
df.tail ()
print(df.head())

df["Dec"]
fig, ax = plt.subplots()
df["Dec"].plot(ax=ax)
ax.set_ylabel("Anomalies")
ax.set_xlabel("Year")
ax.set_title("Temperature Anomalies in December from 1880 to 2025")
plt.show()

plt.savefig("Tutorial 2 plot 1.png")

month = "Dec"
fig, ax = plt.subplots()
ax.axhline(0, color="red")
ax.annotate("1951-1980 average", xy=(0.66, -0.2), xycoords=("figure fraction", "data"))
df[month].plot(ax=ax)
ax.set_title(
    f"Average temperature anomaly in {month} \n in the northern hemisphere (1880-{df.index.max()})"
)
ax.set_ylabel("Annual temperature anomalies");


