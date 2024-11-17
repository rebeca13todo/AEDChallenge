import streamlit as st

# Ejemplo de lista de equipos
equipos = [
    ["Ana", "Marc", "Dani"],
    ["David", "Angel", "Rebeca"],
    ["Clara", "Luis", "Elena"],
    ["Juan", "Sofía", "Mario"]
]

def interfaz(equipos):
    """
    Funció que crea la plataforma streamlit per visualitzar
    els equips creats.
    """

    # Configurar la página de la aplicación
    st.set_page_config(page_title="Visualización de Equipos", page_icon=":star:", layout="wide")

    # Título principal de la aplicación
    st.title("Visualización de Equipos")
    st.write("Aquí puedes ver los diferentes equipos formados para la competición:")

    # Mostrem el nom de cada equip
    for idx, equipo in enumerate(equipos, start=1):
        # Crear una columna para cada equipo
        with st.container():
            st.subheader(f"Equipo {idx}")
            st.write(", ".join(equipo))  # Mostrar los nombres de cada equipo
            st.markdown("---")  # Línea de separación entre equipos

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
        </style>
        """, unsafe_allow_html=True)

result(G, participants)