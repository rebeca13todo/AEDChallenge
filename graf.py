import networkx as nx
from typing import TypeAlias
from distancia import distancia
from participant import load_participants, Participant

data_path = "data/datathon_participants.json"
participants = load_participants(data_path)

PersonesGraph: TypeAlias = nx.Graph

G = nx.Graph()

def arestes_nodes(g: PersonesGraph, particip: list[Participant]):
    """
    Funció que afegeix les persones participants a un graf buit 
    com a nodes i crea una aresta amb totes les demés assignant a 
    aquesta la seva distància corresponent.
    """

    for person1 in particip:
        g.add_node(person1)

        for person2 in particip:
            if person1 != person2:
                g.add_edge(person1, person2, weight = distancia(person1, person2))

    return g