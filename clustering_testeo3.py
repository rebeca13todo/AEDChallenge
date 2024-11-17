import networkx as nx
import random
from sklearn.neighbors import NearestNeighbors



def generar_test_case(n: int = 20, dmax: int = 15):
    '''Dado un número de personas n, generar un test case con distancias aleatorias entre ellas, en el intervalo (0, dmax).
    Un test case es una matriz de distancias entre cada elemento i,j.'''

    distance_matrix: list[list[float]] = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(0, n):
        for j in range(i, n):
            if i == j:
                distance_matrix[i][j] = 0.0
            else:
                d = float(random.randint(0, dmax))
                distance_matrix[i][j] = distance_matrix[j][i] = d

    return distance_matrix


def KNN(dist_matrix: list[list[float]]):
    '''k Nearest Neighbours'''

    # Crear el objeto NearestNeighbors y especificar que vamos a usar una matriz de distancias precomputada
    nn = NearestNeighbors(n_neighbors=4, metric='precomputed')

    # Ajustar el modelo con la matriz de distancias
    nn.fit(dist_matrix)

    # Buscar los 4 vecinos más cercanos para cada punto
    distances, indices = nn.kneighbors(dist_matrix)

    print("Índices de los vecinos más cercanos:")
    print(indices)

    print("Distancias de los vecinos más cercanos:")
    print(distances)


def main():
    M = generar_test_case()
    KNN(M)



if __name__ == "__main__":
    main()





"""
def generar_test_case(n: int = 20, dmax: int = 15):
    '''Dado un número de personas n, generar un test case con distancias aleatorias entre ellas, en el intervalo (0, dmax).
    Un test case es un grafo completo de networkx con cada aresta teninedo una distancia 'distance' asignada.'''

    # Crear el grafo completo con n nodos
    num_personas = n
    G = nx.complete_graph(num_personas)

    # Asignar pesos aleatorios a las aristas (distancias)
    for (u, v) in G.edges():
        G[u][v]['distance'] = random.randint(1, dmax)  # Distancia entre cada nodo (aleatoria entre 0 y dmax)

    return G

def main():
    G = generar_test_case(20, 15)
    print(G)
    print(G.edges.data())

if __name__ == "__main__":
    main()

"""