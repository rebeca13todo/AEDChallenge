import networkx as nx
import random
from sklearn.neighbors import NearestNeighbors

# Generamos datos para el testeo

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