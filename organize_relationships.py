import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os


# This script loads and analyses Caravan data.

# check if folders exist
results_path = "results/"
if not os.path.isdir(results_path):
    os.makedirs(results_path)
figures_path = "figures/"
if not os.path.isdir(figures_path):
    os.makedirs(figures_path)

df = pd.DataFrame()
df["relationship"] = ["Budyko (1974)", "Cuthbert (2019)", "Thompson (2010)"]
df["spatial_scale"] = [1000, 1, 1] # in km but converted to m for plot
df["temporal_scale"] = [30*365, 365, 1] # in days

# spatial scales:
# subcatchment 1 km, small catchment 10 km, large catchment 100 km, regional/continental 1000 km, global 10000 km

# plot
fig = plt.figure(figsize=(3.5, 3), constrained_layout=True)
axes = plt.axes()
#im = axes.scatter(df["spatial_scale"], df["temporal_scale"], s=100, c="tab:purple", alpha=0.5, lw=0)
for i, txt in enumerate(df["relationship"]):
    axes.annotate(txt, (df["spatial_scale"][i]*1.0, df["temporal_scale"][i]*1.0), fontsize=8)
axes.set_xlabel("Spatial gradient [km]")
axes.set_ylabel("Temporal gradient")
#axes.legend(loc='center right', bbox_to_anchor=(1.25, 0.5))
#axes.grid()
axes.set_xscale('log')
axes.set_yscale('log')
axes.set_xticks([1, 10, 100, 1e3, 1e4])
axes.set_xticklabels(['1', '10', '100', '1000', '10000'])
axes.set_xlim([0.1, 1e5])
axes.set_yticks([1, 30, 365, 365*30]) #, 365*1000
axes.set_yticklabels(['Day', 'Month', 'Year', '30y']) #, '1000y'
axes.set_ylim([0.1, 365*1000])
fig.savefig(figures_path + "relationships.png", dpi=600, bbox_inches='tight')
plt.close()

