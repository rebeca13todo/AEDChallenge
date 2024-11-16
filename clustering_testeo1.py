import networkx as nx
import random
from itertools import combinations

# Crear el grafo con 300 nodos
num_personas = 300
G = nx.complete_graph(num_personas)  # Grafo completo donde cada nodo está conectado a todos los demás

# Asignar pesos aleatorios a las aristas (distancias)
for (u, v) in G.edges():
    G[u][v]['weight'] = random.randint(1, 100)  # Peso aleatorio entre 1 y 100

# Función para crear grupos de 4 minimizando la distancia interna
def crear_equipos_min_distancia(G, tam_grupo=4):
    equipos = []
    nodos_asignados = set()  # Para seguir la pista de los nodos ya agrupados

    # Obtener todas las aristas ordenadas por menor peso (distancia)
    aristas_ordenadas = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])

    # Construcción Greedy de equipos
    for u, v, datos in aristas_ordenadas:
        if u not in nodos_asignados and v not in nodos_asignados:
            # Crear un equipo inicial con dos nodos más cercanos
            equipo = [u, v]
            nodos_asignados.update(equipo)

            # Añadir dos personas más al equipo que minimicen la distancia promedio
            candidatos = [n for n in G.nodes if n not in nodos_asignados]
            while len(equipo) < tam_grupo and candidatos:
                mejor_candidato = None
                mejor_distancia = float('inf')

                # Buscar el mejor candidato que minimice la distancia media dentro del equipo
                for candidato in candidatos:
                    # Calcular la distancia promedio si añadimos este candidato
                    distancia_actual = sum(G[candidato][e]['weight'] for e in equipo) / len(equipo)
                    if distancia_actual < mejor_distancia:
                        mejor_distancia = distancia_actual
                        mejor_candidato = candidato

                if mejor_candidato is not None:
                    equipo.append(mejor_candidato)
                    nodos_asignados.add(mejor_candidato)
                    candidatos.remove(mejor_candidato)

            # Añadir el equipo formado a la lista de equipos
            if len(equipo) == tam_grupo:
                equipos.append(equipo)

    # Verificar si quedan personas sin asignar y formar equipos adicionales
    restantes = [n for n in G.nodes if n not in nodos_asignados]
    for i in range(0, len(restantes), tam_grupo):
        equipos.append(restantes[i:i + tam_grupo])

    return equipos

# Ejecutar la función para crear equipos
equipos = crear_equipos_min_distancia(G)

# Mostrar los equipos formados
for i, equipo in enumerate(equipos):
    print(f"Equipo {i+1}: {equipo}")