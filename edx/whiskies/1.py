import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import SpectralCoclustering

whisky = pd.read_csv("whiskies.txt")

whisky["Region"] = pd.read_csv("regions.txt")

#print(whisky.tail())

flavors = whisky.iloc[:, 2:14]

corr_flavors = pd.DataFrame.corr(flavors)

#print(corr_flavors)

plt.figure(figsize=(10, 10))
plt.pcolor(corr_flavors)
plt.colorbar()
plt.savefig("flavor_correlations.png")

corr_whisky = pd.DataFrame.corr(flavors.transpose())

plt.figure(figsize=(10, 10))
plt.pcolor(corr_whisky)
plt.colorbar()
plt.savefig("whisky_correlations.png")

model = SpectralCoclustering(n_clusters=6, random_state=0)

model.fit(corr_whisky)

print(np.sum(model.rows_, axis=1))

whisky["Group"] = pd.Series(model.row_labels_, index=whisky.index)

whisky = whisky.iloc[np.argsort(model.row_labels_)]

whisky = whisky.reset_index(drop=True)

correlations = pd.DataFrame(whisky.iloc[: , 2:14].transpose())

correlations = np.array(correlations)

orig_correlations = np.array(corr_whisky)

plt.pcolor(orig_correlations)
plt.title("Original")
plt.axis("tight")

plt.subplot(1, 2, 2)
plt.pcolor(correlations)
plt.title("Rearranged")
plt.axis("tight")

plt.colorbar()
plt.savefig("correlations.png")
plt.show()