import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Título de la aplicación
st.title("Simulador de Trayectoria de un Mortero")

# Parámetros de entrada
angulo_disparo = st.slider("Ángulo de disparo (grados)", 0, 90, 45)
distancia_maxima = st.number_input("Distancia máxima (m)", min_value=0.0, value=100.0)

# Constantes
g = 9.81  # Aceleración debido a la gravedad (m/s^2)

# Función para calcular la trayectoria
def calcular_trayectoria(angulo, distancia):
    angulo_rad = np.radians(angulo)
    t_total = 2 * (distancia * np.sin(angulo_rad)) / g  # Tiempo total de vuelo
    t = np.linspace(0, t_total, num=100)  # Vector de tiempo
    x = distancia * (t / t_total)  # Posición horizontal
    y = (distancia * np.tan(angulo_rad)) - (0.5 * g * (t ** 2))  # Posición vertical
    return x, y

# Botón para calcular y mostrar la trayectoria
if st.button("Calcular trayectoria"):
    x, y = calcular_trayectoria(angulo_disparo, distancia_maxima)

    # Graficar la trayectoria
    plt.figure(figsize=(10, 5))
    plt.plot(x, y)
    plt.title("Trayectoria del Mortero")
    plt.xlabel("Distancia (m)")
    plt.ylabel("Altura (m)")
    plt.xlim(0, distancia_maxima)
    plt.ylim(0, (distancia_maxima * np.tan(np.radians(angulo_disparo))) + 10)
    plt.grid()
    st.pyplot(plt)
