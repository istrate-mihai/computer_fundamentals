import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

original_set            = -2 * np.random.rand(100, 2)
second_set              = 1 + 2 * np.random.rand(50, 2)
original_set[50:100, :] = second_set

kmean = KMeans(n_clusters = 2)
kmean.fit(original_set)
print(kmean.cluster_centers_)
print(kmean.labels_)

for i in set(kmean.labels_):
    index = (kmean.labels_ == i)
    plt.plot(original_set[index, 0], original_set[index, 1], 'o')

plt.plot(kmean.cluster_centers_[0][0], kmean.cluster_centers_[0][1], '*', c = 'r', ms = 10)
plt.plot(kmean.cluster_centers_[1][0], kmean.cluster_centers_[1][1], '*', c = 'r', ms = 10)
plt.show()

sample = np.array([[-1.4, -1.4]])
print(kmean.predict(sample))

another_sample = np.array([[2.5, 2.5]])
print(kmean.predict(another_sample))

data     = [25., 5., 150., 100.]
x_values = range(len(data))
plt.bar(x_values, data, width = 1.)
plt.show()

data = [
    [8., 57., 22., 10.],
    [16., 7., 32., 40.],
]
x_values = np.arange(4)
plt.bar(x_values + 0.00, data[0], color = 'r', width = 0.30)
plt.bar(x_values + 0.00, data[1], color = 'y', width = 0.30)
plt.show()

data = np.random.rand(50)
plt.boxplot(data)
plt.show()

data   = [500, 200, 250]
labels = ["Agriculture", "Aide", "News"]
plt.pie(data, labels = labels, autopct = '%1.1f%%')
plt.show()

n      = 10
x      = np.random.rand(n)
y      = np.random.rand(n)
colors = np.random.rand(n)
area   = np.pi * (60 * np.random.rand(n)) ** 2
plt.scatter(x, y, s = area, c = colors, alpha = 0.5)
