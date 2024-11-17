import networkx as nx
from typing import TypeAlias
from distancia import distancia
from participant import load_participants, Participant
import streamlit as st
import pandas as pd

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

def equips_creats(g: PersonesGraph) -> list[list[Participant]]:
    """
    Funció que crea els equips mitjançant un algorisme
    de clustering. 
    """
    tam: int = 4
    equips = []
    n_assignats = set()

    sort_arestes = sorted(g.edges(data=True), key=lambda x: x[2]['weight'])


    for u, v, data in sort_arestes:
        if u not in n_assignats and v not in n_assignats:
            equip = [u, v]
            n_assignats.update(equip)

            candidats = [n for n in g.nodes if n not in n_assignats]
            while len(equip) < tam and candidats:
                millor_candidat = None
                millor_distancia = float('inf')

                for c in candidats:
                    dist_act = sum(g[c][e]['weight'] for e in equip) / len(equip)
                    if dist_act < millor_distancia:
                        millor_distancia = dist_act
                        millor_candidat = c

                if millor_candidat is not None:
                    equip.append(millor_candidat)
                    n_assignats.add(millor_candidat)
                    candidats.remove(millor_candidat)

            if len(equip) == tam:
                equips.append(equip)

    resta = [n for n in g.nodes if n not in n_assignats]
    for i in range(0, len(resta), tam):
        equips.append(resta[i:i + tam])

    return equips
                
def interfaz(equipos: list[list[str]]):
    """
    Funció que crea la plataforma streamlit per visualitzar
    els equips creats.
    """

    st.set_page_config(page_title="Equipos para la Competición", page_icon=":trophy:", layout="wide")

    # Títul de la pàgina
    st.title("Equips per la Competició")
    st.write("Equips formats per a la competició mitjançant l'algorisme:")

    df = pd.DataFrame(equipos)

    # Veiem la taula amb Streamlit
    st.dataframe(df, width=700) 
    
    st.markdown("""
        <style>
            .css-18e3th9 {
                background-color: #f0f0f5;
                border-radius: 10px;
                padding: 10px;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
            }
            .css-10trblm {
                color: #444;
                font-family: 'Arial', sans-serif;
            }
            .css-1d391kg {
            font-size: 14px;  /* Tamaño más pequeño para la tabla */
            }
            .css-1h3bh6l {
                font-size: 14px;  /* Tamaño más pequeño para el texto */
            }
            .stDataFrame {
                font-size: 14px;  /* Tamaño de la fuente de las celdas */
            }
            body {
                background: url('https://www.w3schools.com/w3images/forest.jpg') no-repeat center center fixed;
                background-size: cover;
                height: 100%;
                margin: 0;
            }
        </style>
        """, unsafe_allow_html=True
    )


def result(g: PersonesGraph, particip: list[Participant]) -> list[list[str]] | None:
    """
    Funció que crea crida a les funciones per crear un graf entre els participants,
    els relaciona entre sí en funció dels seus atributs en comú, els agrupa en equips 
    de quatre i els traça en una interfície de Streamlit
    """

    # Cridem la funció per montar un graf amb els participants
    graf = arestes_nodes(g, particip)

    # Cridem la funció per montar els equips
    equips_m: list[list[Participant]] = equips_creats(graf)

    # Seleccionem els noms dels integrants dels equips
    equips_m_noms: list[list[str]] = [[equips_m[i][j].name for j in range(len(equips_m[0]))] for i in range(len(equips_m))]

    # Creem una interfície en Streamlit
    equip_int = interfaz(equips_m_noms)

    if equip_int is None: return print("Els equips encara no han sigut creats!")
    else:
        return equip_int


# Obentim els resultats 
result(G, participants)