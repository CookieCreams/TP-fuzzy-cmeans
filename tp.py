import numpy as np
import cv2
import matplotlib.pyplot as plt

def initialise_matrice_app(nb_samples, nb_clusters):
    matrice_app = np.random.rand(nb_samples, nb_clusters)
    matrice_app = matrice_app / matrice_app.sum(axis=1, keepdims=True)
    return matrice_app

def calcul_centres(data, matrice_app, m):
    um = matrice_app ** m
    numerator = um.T @ data
    somme_ponderees = um.sum(axis=0) #Calcul la somme des poids d'appartenance pour chaque cluster
    denominateur = somme_ponderees[:, np.newaxis] #Reshaper pour correspondre à la dimension du numérateur (nombre de clusters, 1)
    return numerator / denominateur

def update(data, centres, m):
    nb_samples = data.shape[0]
    nb_clusters = centres.shape[0]
    matrice_app = np.zeros((nb_samples, nb_clusters))

    for i in range(nb_clusters):
        diff = data - centres[i]
        dist = np.sqrt(np.sum(diff ** 2, axis=1)).reshape(-1, 1)

        temp_sum = np.zeros(nb_samples)
        for k in range(nb_clusters):
            centre_diff = data - centres[k]
            centre_dist = np.sqrt(np.sum(centre_diff ** 2, axis=1)).reshape(-1, 1)
            ratio = dist / centre_dist
            temp_sum += (ratio ** (2 / (m - 1))).flatten()

        matrice_app[:, i] = 1 / temp_sum

    return matrice_app


def fuzzy_cmeans(data, nb_clusters, m, max_iter=10):
    matrice_app = initialise_matrice_app(data.shape[0], nb_clusters)
    for iteration in range(max_iter):
        centres = calcul_centres(data, matrice_app, m)
        new_matrice_app = update(data, centres, m)
        matrice_app = new_matrice_app
    return centres, matrice_app

#Charger image
image = cv2.imread('milky-way.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
data = image.reshape((-1, 3))

#Parametres
nb_clusters = 5
m = 1.4
centres, matrice_app = fuzzy_cmeans(data, nb_clusters, m)

fig, axs = plt.subplots(1, nb_clusters, figsize=(15, 5))
for i in range(nb_clusters):
    cluster_image = np.zeros_like(data)
    cluster_image[np.argmax(matrice_app, axis=1) == i] = centres[i]
    cluster_image = cluster_image.reshape(image.shape)
    
    #heatmap
    heatmap = matrice_app[:, i].reshape(image.shape[:2])
    
    axs[i].imshow(cluster_image)
    axs[i].imshow(heatmap, cmap='hot')
    axs[i].set_title(f'Cluster {i + 1}')
    axs[i].axis('off')

plt.show()
