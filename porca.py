import streamlit as st
import pandas as pd

# Ejemplo de lista de equipos
equipos = [
    ["Ana", "Marc", "Dani"],
    ["David", "Angel", "Rebeca"],
    ["Clara", "Luis", "Elena"],
    ["Juan", "Sofía", "Mario"]
]

# Crear DataFrame para la tabla
data = {
    "Equipo": [f"Equipo {idx + 1}" for idx in range(len(equipos))],
    "Integrantes": [", ".join(equipo) for equipo in equipos]
}
df = pd.DataFrame(data)

# Configurar la página de la aplicación
st.set_page_config(page_title="Equipos para la Competición", page_icon=":trophy:", layout="wide")

# Título principal de la aplicación
st.title("Equipos para la Competición")
st.write("Visualización de los equipos formados para la competición:")

# Mostrar la tabla con Streamlit
st.dataframe(df, width=700)  # Ajustar el ancho de la tabla para que sea más compacta

# CSS personalizado para reducir el tamaño de la fuente de la tabla
st.markdown(
    """
    <style>
        .css-1d391kg {
            font-size: 14px;  /* Tamaño más pequeño para la tabla */
        }
        .css-1h3bh6l {
            font-size: 14px;  /* Tamaño más pequeño para el texto */
        }
        .stDataFrame {
            font-size: 14px;  /* Tamaño de la fuente de las celdas */
        }
    </style>
    """,
    unsafe_allow_html=True
)
