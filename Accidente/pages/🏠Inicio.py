# pages/1-🏠Inicio.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(
    page_title="Cargador de Datos",
    layout="wide"
)

tab1, tab2, tab3 = st.tabs(["Inicio", "Reportes", "Gráficos"])

with tab1:
    @st.cache_data
    def load_data(file):
        if file.name.endswith('.csv'):
            return pd.read_csv(file)
        elif file.name.endswith('.xlsx'):
            return pd.read_excel(file)
        elif file.name.endswith('.json'):
            return pd.read_json(file)
        else:
            raise ValueError("Formato no soportado")

    st.title("📤 Cargar Datos")
    uploaded_file = st.file_uploader("Sube tu archivo (CSV, Excel, JSON)", type=["csv", "xlsx", "json"])

    if uploaded_file:
        try:
            data = load_data(uploaded_file)
            st.session_state['data'] = data
            st.session_state['file_name'] = uploaded_file.name
            st.success("¡Datos cargados correctamente!")
            col1, col2, col3 = st.columns(3)
            col1.metric("Filas", data.shape[0])
            col2.metric("Columnas", data.shape[1])
            col3.metric("Tamaño", f"{uploaded_file.size / 1024:.2f} KB")
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.info("Por favor, sube un archivo para comenzar.")

with tab2:
    st.title("Reportes")
    if 'data' in st.session_state:
        data = st.session_state['data']
        st.write("Primeras filas de los datos:")
        st.dataframe(data.head())
        st.write("Últimas filas de los datos:")
        st.dataframe(data.tail())
        st.write("Resumen de los datos:")
        st.write(data.describe())
        st.write("Columnas del DataFrame:")
        st.write(data.columns.tolist())
        st.write("Datos nulos por columna:")
        st.write(data.isnull().sum())
        st.write("Tipos de datos por columna:")
        st.write(data.dtypes)
    else:
        st.warning("No hay datos disponibles para mostrar.")

with tab3:
    st.title("Gráficos")
    if 'data' in st.session_state:
        data = st.session_state['data']
        numeric_cols = data.select_dtypes(include=[np.number]).columns.tolist()
        if numeric_cols:
            selected_col = st.selectbox("Selecciona una columna numérica para graficar:", numeric_cols)
            chart_type = st.selectbox("Selecciona el tipo de gráfico:", ["Línea", "Barras", "Histograma", "Caja y Bigotes", "Dispersión"])
            if chart_type == "Línea":
                st.line_chart(data[selected_col])
            elif chart_type == "Barras":
                st.bar_chart(data[selected_col])
            elif chart_type == "Histograma":
                fig, ax = plt.subplots()
                ax.hist(data[selected_col].dropna(), bins=30)
                st.pyplot(fig)
            elif chart_type == "Caja y Bigotes":
                fig, ax = plt.subplots()
                ax.boxplot(data[selected_col].dropna())
                st.pyplot(fig)
            elif chart_type == "Dispersión":
                if len(numeric_cols) > 1:
                    x_col = st.selectbox("Columna eje X:", numeric_cols)
                    y_col = st.selectbox("Columna eje Y:", numeric_cols)
                    fig, ax = plt.subplots()
                    ax.scatter(data[x_col], data[y_col])
                    st.pyplot(fig)
                else:
                    st.warning("Se requieren al menos dos columnas numéricas.")
        else:
            st.warning("No hay columnas numéricas disponibles para graficar.")
    else:
        st.warning("No hay datos cargados para generar gráficos.")

st.markdown("---")
st.caption("Panel desarrollado con Streamlit y Plotly | © 2023 Análisis Big Data")