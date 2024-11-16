import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist

def kmeans_fixed_size(X, num_clusters, group_size=4):
    # Paso 1: Inicialización de KMeans con un número adecuado de grupos
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(X)
    
    # Paso 2: Asignación inicial de los puntos a los clústeres
    labels = kmeans.labels_
    
    # Paso 3: Reorganizar los puntos para asegurar que cada grupo tenga el tamaño deseado
    cluster_sizes = np.bincount(labels)
    
    # Verificar que todos los grupos tengan tamaño correcto (esto puede ser un desafío si num_clusters no es adecuado)
    # Si algún grupo tiene más de 'group_size' puntos, redistribuirlos a otros grupos
    while any(cluster_sizes != group_size):
        for i, size in enumerate(cluster_sizes):
            if size > group_size:
                # Encontrar otro grupo con menos de group_size
                for j in range(len(labels)):
                    if labels[j] == i:
                        # Mover punto a otro grupo
                        new_group = find_best_cluster(X[j], kmeans.cluster_centers_, labels)
                        if cluster_sizes[new_group] < group_size:
                            labels[j] = new_group
                            cluster_sizes[i] -= 1
                            cluster_sizes[new_group] += 1
                            break
    
    # Paso 4: Calcular las distancias internas para verificar que la partición es óptima
    # Usamos cdist para calcular las distancias entre cada punto y su centroide
    distances = cdist(X, kmeans.cluster_centers_)
    
    # Retornar la nueva partición con las etiquetas ajustadas
    return labels, kmeans.cluster_centers_, distances

def find_best_cluster(point, centroids, labels):
    # Función para encontrar el mejor grupo para un punto
    # Busca el clúster que minimiza la distancia al centroide
    distances = np.linalg.norm(centroids - point, axis=1)
    best_cluster = np.argmin(distances)
    return best_cluster

# Ejemplo de uso:
np.random.seed(42)

# Datos de ejemplo (10 puntos en 2 dimensiones)
X = np.random.rand(10, 2)

# Llamar a la función con el número de grupos deseado
num_clusters = 3  # Intentamos dividir en 3 grupos
labels, centroids, distances = kmeans_fixed_size(X, num_clusters, group_size=4)

print("Etiquetas de los clústeres:", labels)
print("Centroides de los clústeres:", centroids)
