import numpy as np
import streamlit as st
import pandas as pd
st.set_page_config(page_title="Predicción Gasolina", page_icon="⛽", layout="centered")

st.title("⛽ Predicción del precio de la gasolina")
st.image("gasolina.jpg", caption="Precio de la gasolina.", use_column_width=True)

st.markdown("---")

# --- Datos de referencia ---
st.header("Datos de referencia")
st.image("Relacion de estados.png", caption="Estados de México", use_column_width=True)

# --- Entrada de usuario ---
st.header("📊 Ingrese los datos para la predicción")

col1, col2, col3 = st.columns(3)

with col1:
    año = st.slider("Año", min_value=2017, max_value=2030, value=2024, step=1)

with col2:
    meses = {
        "Enero": 1, "Febrero": 2, "Marzo": 3, "Abril": 4,
        "Mayo": 5, "Junio": 6, "Julio": 7, "Agosto": 8,
        "Septiembre": 9, "Octubre": 10, "Noviembre": 11, "Diciembre": 12
    }
    mes_nombre = st.selectbox("Mes", list(meses.keys()))
    mes = meses[mes_nombre]

with col3:
    entidad = st.number_input("Entidad (0-32)", min_value=0, max_value=32, value=0, step=1)

# --- Construcción del DataFrame de entrada ---
df = pd.DataFrame({
    "Año": [año],
    "Mes": [mes],
    "Entidad": [entidad]
})

# --- Modelo ---
precio = pd.read_csv("GASOLINA2.csv", encoding="latin-1")
X = precio.drop(columns="PRECIO")
y = precio["PRECIO"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)
lr = LinearRegression()
lr.fit(X_train, y_train)

# --- Predicción ---
prediccion = lr.predict(df)[0]

# --- Resultados ---
st.markdown("---")
st.subheader("💡 Resultado de la predicción")
st.metric(label="Precio estimado de la gasolina", value=f"${prediccion:,.2f} MXN")
