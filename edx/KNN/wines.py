import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as ss
from matplotlib.colors import ListedColormap
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import scale


def majority_vote_fast(votes):
    mode, count = ss.mstats.mode(votes)
    return mode


def distance(p1, p2):
    return np.sqrt(np.sum(np.power(p2 - p1, 2)))


def find_nearest_neighbors(p, points, k=5):
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = distance(p, points[i])
    ind = np.argsort(distances)
    return ind[:k]


def knn_predict(p, points, outcomes, k=5):
    ind = find_nearest_neighbors(p, points, k)
    return majority_vote_fast(outcomes[ind])[0]


def accuracy(predictions, outcomes):
    return np.mean(predictions == outcomes) * 100

data = pd.read_csv(r"C:\Users\smtty\OneDrive\Belgeler\Edx\KNN\wine.csv", index_col=0)

data["is_red"] = (data["color"] == "red").astype(int)

numeric_data = data.drop(columns=["color", "quality", "high_quality"])

scaled_data = scale(numeric_data)
numeric_data = pd.DataFrame(scaled_data, columns=numeric_data.columns)


pca = PCA(n_components=2)
principal_components = pca.fit_transform(numeric_data)

observation_colormap = ListedColormap(["red", "blue"])
x = principal_components[:, 0]
y = principal_components[:, 1]

plt.figure(figsize=(8, 6))
plt.title("Principal Components of Wine")
plt.scatter(
    x,
    y,
    alpha=0.2,
    c=data["high_quality"],
    cmap=observation_colormap,
    edgecolors="none",
)
plt.xlim(-8, 8)
plt.ylim(-8, 8)
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.show()


knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(numeric_data, data["high_quality"])

library_prediction = knn.predict(numeric_data)
library_acc = accuracy(library_prediction, data["high_quality"])
print(f"Accuracy of Scikit-Learn KNN Model: {library_acc:.2f}%")


n_rows = data.shape[0]
random.seed(123)
selection = random.sample(range(n_rows), 10)

predictors = np.array(numeric_data)
training_indices = [i for i in range(len(predictors)) if i not in selection]
outcomes = np.array(data["high_quality"])

my_predictions = np.array(
    [
        knn_predict(
            p,
            predictors[training_indices, :],
            outcomes[training_indices],
            k=5,
        )
        for p in predictors[selection]
    ]
)

percentage = accuracy(my_predictions, data.high_quality.iloc[selection])
print(f"Accuracy of Our Custom KNN Model (on 10 Test Samples): {percentage:.2f}%")