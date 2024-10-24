### Introduction

Fuzzy C-Means est une technique de segmentation utilisée pour diviser des données en plusieurs clusters. Contrairement à d'autres méthodes de clustering, cette méthode permet à chaque point de données d'appartenir à plusieurs clusters avec des degrés d'appartenance différents. On va appliquer cette méthode sur l’image milky-way en couleurs et verrons la segmentation effectuée sur cette image à travers les différentes clusters.

### Implémentation
2 paramètres doivent être définis et donner à notre algorithme: le nombre de clusters et le paramètre fuzzy m qui doit être supérieur à 1. Ces paramètres peuvent être modifiés.

## Initialisation de la matrice d’appartenance
On initialise la matrice d’appartenance dont les valeurs sont comprises entre 0 et 1, et que la somme des appartenances soit égale à 1 pour chaque pixel.

## Calcul des centres de clusters
On calcul ensuite les centres des clusters en utilisant cette formule:
![Capture d'écran 2024-10-24 214839](https://github.com/user-attachments/assets/2013aec8-c449-4507-9487-8f2164108d8b)

Elle calcule les centres du cluster en fonction de la matrice d’appartenance, des pixels de l’image et du paramètre fuzzy m.

## M ise à jour des appartenances
Les appartenances sont mises à jour en calculant la distance euclidienne entre chaque pixel et les centres des clusters, et en ajustant les valeurs d'appartenance en conséquence .Puis on calcule le ratio entre la distance d'un pixel à un centre donné et la distance de ce même pixel à tous les autres centres. On obtient ensuite les nouvelles valeurs d’appartenance. 
![Capture d'écran 2024-10-24 235659](https://github.com/user-attachments/assets/b02eade1-79a9-4158-980e-aa175bda1ea7)


Tant que la convergence n’est pas atteinte ou que le nombre d’itération max ne soit pas atteint, l’algorithme répète les étapes de calcul des centres et de mise à jour.
On obtient finalement des images segmentées pour chaque cluster visible avec une heatmap.

### Résultats
Voici un exemple de résultat avec m=1.4 et le nb_cluster=2:

![Capture d'écran 2024-10-25 000252](https://github.com/user-attachments/assets/85a6d5ff-a53c-470e-af06-5fb1791767b6)


Avec m=1.4 et nb_cluster=5:

![Capture d'écran 2024-10-25 000355](https://github.com/user-attachments/assets/506ba615-ea3e-4678-a00c-48e37b418d86)


Avec m=50 et nb_cluster=5:

![Capture d'écran 2024-10-25 000724](https://github.com/user-attachments/assets/0c4ff144-9e2f-419f-83cb-9fe80f56e0c0)


On remarque que lorsque m a une valeur élevée, on a du mal à bien distinguer les différentes segmentations à travers les clusters. Les frontières entre les clusters deviennent plus flous.
