import numpy as np
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Predicción Gasolina", page_icon="⛽", layout="centered")

st.title("⛽ Predicción del precio de la gasolina")
st.image("gasolina.jpg", caption="Precio de la gasolina.")

#Datos de referencia
st.header("Datos de referencia")
st.image("Relacion de estados.png", caption="Estados de México")

st.header("📊 Ingrese los datos para la predicción")

def user_input_features():
  # Entrada
  Año = st.slider('Año',  min_value=2017, max_value=3000, value = 2024, step = 1)
  Meses = {
    "Enero": 1, "Febrero": 2, "Marzo": 3, "Abril": 4,
    "Mayo": 5, "Junio": 6, "Julio": 7, "Agosto": 8,
    "Septiembre": 9, "Octubre": 10, "Noviembre": 11, "Diciembre": 12
  }

  mes_nombre = st.selectbox("Mes", list(Meses.keys()))
  Mes = Meses[mes_nombre]

  Entidad = st.number_input('Entidad (0-32):', min_value=0, max_value=32, value = 0, step = 1)


  user_input_data = {'Año': Año,
                     'Mes': Mes,
                     'Entidad': Entidad}

  features = pd.DataFrame(user_input_data, index=[0])

  return features

df = user_input_features()

Precio =  pd.read_csv('GASOLINA2.csv', encoding='latin-1')
X = Precio.drop(columns='PRECIO')
y = Precio['PRECIO']

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)
LR = LinearRegression()
LR.fit(X_train,y_train)

b1 = LR.coef_
b0 = LR.intercept_
prediccion = b0 + b1[0]*df.Año + b1[1]*df.Mes + b1[2]*df.Entidad

st.subheader("💡 Resultado de la predicción")
st.markdown(
    f"""
<div style="text-align: center; background-color: #F2F4F4; padding: 20px; border-radius: 15px;">
<h3 style="color: #D35400;">El precio será:</h3>
<p style="font-size: 28px; font-weight: bold; color: #1F618D;">${prediccion.values[0]:.2f} MXN</p>
</div>
    """, 
    unsafe_allow_html=True
)

