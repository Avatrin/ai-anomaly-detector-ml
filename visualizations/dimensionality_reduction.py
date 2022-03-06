import sklearn 
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def visualize_tsne(perplexity):
  model = TSNE(perplexity=perplexity)
  tsne_result = model.fit_transform(table_df.values)
  table_df['tsne-one'] = tsne_result[:,0]
  table_df['tsne-two'] = tsne_result[:,1] 
  plt.figure(figsize=(16,10))
  sns.scatterplot(
    x="tsne-one", y="tsne-two",
    palette = sns.color_palette("flare", as_cmap=True),
    data=table_df,
    legend="full",
    )
