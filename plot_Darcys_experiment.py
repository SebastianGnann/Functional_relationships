# import all necessary Python packages
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
#import ipywidgets as widgets
import os

# check if folders exist
results_path = "results/"
if not os.path.isdir(results_path):
    os.makedirs(results_path)

figures_path = "figures/"
if not os.path.isdir(figures_path):
    os.makedirs(figures_path)

# load data into workspace
df = pd.read_csv("results/Darcys_Experiment_1.csv", sep=',')
df["Flow"] = df["Flow"]/(np.pi*(.35/2)**2*60*1000) # convert to m/s
df2 = pd.read_csv("results/Darcys_Experiment_2.csv", sep=',')
df2["Flow"] = df2["Flow"]/(np.pi*(.35/2)**2*60*1000) # convert to m/s
df.head()
#df2.head()

### English version for publication ###
# fit data
def plot_linear_regression(X,Y,color,text):
    model = LinearRegression(fit_intercept=False)
    model.fit(X, Y)
    predictions = model.predict(X)
    slope = model.coef_[0]
    ax.scatter(X, Y, facecolors='none', edgecolors=color, s=20)
    ax.plot(X, predictions, '-', c=color, label=text+f', K = {slope:.1e} m/s') #.2f

# plot data
fig, ax = plt.subplots(figsize=(4, 3))
plot_linear_regression(df.loc[df["Set"]==1,"Pressure"].values.reshape(-1, 1)/0.58, df.loc[df["Set"]==1,"Flow"],'black','Set 1.1')
plot_linear_regression(df.loc[df["Set"]==2,"Pressure"].values.reshape(-1, 1)/1.14, df.loc[df["Set"]==2,"Flow"],'black','Set 1.2')
plot_linear_regression(df.loc[df["Set"]==3,"Pressure"].values.reshape(-1, 1)/1.71, df.loc[df["Set"]==3,"Flow"],'black','Set 1.3')
plot_linear_regression(df.loc[df["Set"]==4,"Pressure"].values.reshape(-1, 1)/1.70, df.loc[df["Set"]==4,"Flow"],'black','Set 1.4')
plot_linear_regression(df2.loc[df2["Set"]==1,"Pressure difference"].values.reshape(-1, 1)/1.1, df2.loc[df2["Set"]==1,"Flow"],'black','Set 2.1')
ax.set_xlim([0, 20])
ax.set_ylim([0, 0.006])
plt.xlabel('Pressure difference / column length [-]')
plt.ylabel('Specific discharge [m/s]')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
#plt.grid(alpha=0.5)
plt.legend(bbox_to_anchor=(1.05, 0.76))
fig.savefig(figures_path + "Darcys_experiment.png", dpi=600, bbox_inches='tight')
