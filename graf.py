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
                

def result(g: PersonesGraph, particip: list[Participant]) -> list[list[str]]:

    graf = arestes_nodes(g, particip)

    equips_m: list[list[Participant]] = equips_creats(graf)

    equips_m_noms: list[list[str]] = [[equips_m[i][j].name for j in range(len(equips_m[0]))] for i in range(len(equips_m))]

    equip_int = interfaz(equips_m_noms)

    return equip_int



def interfaz(equipos):
    """
    Funció que crea la plataforma streamlit per visualitzar
    els equips creats.
    """

    # Configurar la página de la aplicación
    st.set_page_config(page_title="Equipos para la Competición", page_icon=":trophy:", layout="wide")

    # Título principal de la aplicación
    st.title("Equipos para la Competición")
    st.write("Visualización de los equipos formados para la competición:")

    df = pd.DataFrame(equipos)

    # Mostrar la tabla con Streamlit
    st.dataframe(df, width=700)  # Ajustar el ancho de la tabla para que sea más compacta


    # Estilo adicional con Streamlit
    
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
    
result(G, participants)