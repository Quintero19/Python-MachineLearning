# app.py
import streamlit as st
import pandas as pd
from io import StringIO
import os
from PIL import Image 

# Configuración de la página
st.set_page_config(
    page_title="Sistema de Gestión de Datos",
    layout="wide",
    page_icon="📊"
)

def main():
    # Header con estilo
    st.title("📊 Sistema de Gestión de Datos")
    st.markdown("---")

    # Sección de bienvenida
    col1, col2 = st.columns([3, 2])

    with col1:
        st.header("Bienvenido")
        st.write("""
        Este sistema te permite:
        - Cargar archivos en formatos CSV, Excel o JSON
        - Visualizar y explorar tus datos
        - Generar análisis automáticos
        - Exportar resultados
        """)
        st.info("💡 Comienza subiendo tu archivo en el menú de inicio")

    with col2:
        st.image(
            "https://img.datacentermarket.es/wp-content/uploads/2025/01/16115523/Bases-de-datos-como-Servicio-3.jpeg",
            caption=""
        )

if __name__ == "__main__":
    main()

# Pie de página
st.markdown("---")
st.caption("Panel desarrollado con Streamlit y Plotly | © 2023 Análisis Big Data")