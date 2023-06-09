# -*- coding: utf-8 -*-
"""Shoppers Data Analysis

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ai-4nCi3dCZOGLJ9khiTlXW30tPokpra
"""

from sklearn.cluster import KMeans, DBSCAN
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load the dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00468/online_shoppers_intention.csv"
data = pd.read_csv(url)

#Histogram for ProductRelated
plt.hist(data['ProductRelated'], bins=50)
plt.xlabel('ProductRelated')
plt.ylabel('Frequency')
plt.title('Distribution of ProductRelated in Online Shoppers Intention dataset by Riya')
plt.show()

# Create a scatter plot of BounceRates vs ExitRates
plt.scatter(data["BounceRates"], data["ExitRates"])
plt.xlabel("BounceRates")
plt.ylabel("ExitRates")
plt.title("BounceRates vs ExitRates in Online Shoppers Intention dataset by Riya")
plt.show()

# Create a box plot of ProductRelated vs Month
sns.boxplot(x="Month", y="ProductRelated", data=data)
plt.xlabel("Month")
plt.ylabel("ProductRelated")
plt.title("ProductRelated vs Month in Online Shoppers Intention dataset by Riya")
plt.show()

# Preprocess the dataset
data = data.drop(columns=['Administrative', 'Informational', 'ProductRelated', 'SpecialDay'])
X = data.iloc[:,:-1].values
y = data.iloc[:,-1].values

# Encode categorical variables
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 10] = labelencoder_X.fit_transform(X[:, 10])
onehotencoder = OneHotEncoder(categories='auto')
X = onehotencoder.fit_transform(X).toarray()

# Apply PCA for visualization
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Visualize the dataset using scatter plot
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y)
plt.title('PCA plot of Online Shoppers Intention Dataset by Riya')
plt.show()

# Cluster the dataset using KMeans
kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
kmeans_labels = kmeans.fit_predict(X)

# Evaluate the KMeans clustering using silhouette score
silhouette_avg = silhouette_score(X, kmeans_labels)
print('Silhouette Score for KMeans clustering:', silhouette_avg)

# Visualize the KMeans clustering using scatter plot
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=kmeans_labels)
plt.title('KMeans clustering of Online Shoppers Intention Dataset by Riya')
plt.show()

# Cluster the dataset using DBSCAN
dbscan = DBSCAN(eps=3, min_samples=100)
dbscan_labels = dbscan.fit_predict(X)

# Evaluate the DBSCAN clustering using silhouette score
silhouette_avg = silhouette_score(X, dbscan_labels)
print('Silhouette Score for DBSCAN clustering:', silhouette_avg)

# Visualize the DBSCAN clustering using scatter plot
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=dbscan_labels)
plt.title('DBSCAN clustering of Online Shoppers Intention Dataset by Riya')
plt.show()

# Classify the dataset using Naive Bayes, KNN, and Decision Tree algorithms
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Naive Bayes
print("running NB")
nb_classifier = GaussianNB()
nb_scores = cross_val_score(nb_classifier, X_train, y_train, cv=5)
nb_mean_score = nb_scores.mean()
nb_classifier.fit(X_train, y_train)
nb_y_pred = nb_classifier.predict(X_test)
nb_accuracy = accuracy_score(y_test, nb_y_pred)
print('Naive Bayes cross-validation score:', nb_mean_score)
print('Naive Bayes test accuracy:', nb_accuracy)

# KNN
print("running KNN")
knn_classifier = KNeighborsClassifier(n_neighbors=5)
knn_scores = cross_val_score(knn_classifier, X_train, y_train, cv=5)
print("Cross-validation scores: {}".format(knn_scores))
print("Mean cross-validation score: {:.2f}".format(knn_scores.mean()))
knn_classifier.fit(X_train, y_train)
test_score = knn_classifier.score(X_test, y_test)

print("Test set score: {:.2f}".format(test_score))