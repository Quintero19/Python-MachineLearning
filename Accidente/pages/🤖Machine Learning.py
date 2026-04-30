import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

st.set_page_config(
    page_title="Modelado de Datos",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Panel de Machine Learning")
st.markdown("---")

if 'data' not in st.session_state:
    st.warning("No se han cargado datos desde la página de inicio.")
    st.stop()

data = st.session_state['data']

st.subheader("1. Selección de variables")
columnas_numericas = data.select_dtypes(include=[np.number]).columns.tolist()

x_col = st.selectbox("Variable independiente (X):", columnas_numericas)
y_col = st.selectbox("Variable dependiente (Y):", columnas_numericas, index=1)

if st.button("Entrenar modelo"):
    X = data[[x_col]].dropna()
    y = data[y_col].loc[X.index]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    st.success("Modelo entrenado correctamente")

    st.write(f"**Coeficiente (pendiente):** {model.coef_[0]:.2f}")
    st.write(f"**Intercepto:** {model.intercept_:.2f}")
    st.write(f"**R² Score:** {r2_score(y_test, y_pred):.2f}")

    fig, ax = plt.subplots()
    ax.scatter(X_test, y_test, label="Datos reales")
    ax.plot(X_test, y_pred, color='red', label="Predicción")
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.legend()
    st.pyplot(fig)