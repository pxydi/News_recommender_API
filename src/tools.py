# Written by P. Xydi, April 2022

######################################
# Import libraries
######################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import matplotlib.cm as cm
color_1 = cm.get_cmap("Set2")(2) # set blue 
color_2 = cm.get_cmap("Set2")(1) # set orange
from sklearn.metrics import ConfusionMatrixDisplay

######################################
def sample_distribution(labels):
    """
    Plots the distribution of samples in the provide variable (categorical)
    
    Input:
    - labels : list, list of target values
    
    """
######################################

    w = pd.value_counts(labels)

    # Barplot and font specifications
    barplot_specs = {"color": color_2, "alpha": 0.7, "edgecolor": "grey"}
    label_specs   = {"fontsize": 12}
    title_specs   = {"fontsize": 14, "fontweight": "bold", "y": 1.02}

    plt.figure(figsize=(8,4.5))
    sns.barplot(x=w.index,y=w.values, **barplot_specs);
    plt.ylabel('Number of samples',**label_specs);
    plt.xticks(rotation=45)
    plt.yscale('log')
    plt.title('Sample distribution in category column',**title_specs);

#######################
# Plot cosine similarity using heatmaps

def plot_similarity(features):
#################################
    plt.figure(figsize=(20,20))
    corr = features 
    mask = np.triu(np.ones_like(corr, dtype=bool))

    g = sns.heatmap(
        corr,
        vmin=0,
        vmax=features.max().max(),
        cmap= "YlOrRd"
    )
    g.set_title("Semantic Textual Similarity")

