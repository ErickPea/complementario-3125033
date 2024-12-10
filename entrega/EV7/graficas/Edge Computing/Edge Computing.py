import matplotlib.pyplot as plt
import numpy as np

# Datos
años = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])
america_norte = np.array([25, 28, 30, 32, 34, 35, 36, 38, 40])  # América del Norte (%)
asia = np.array([10, 12, 15, 18, 20, 22, 24, 25, 27])  # Asia (%)
europa = np.array([15, 17, 20, 22, 24, 25, 26, 28, 29])  # Europa (%)

# Gráfica para América del Norte
plt.figure(figsize=(8, 6))
plt.scatter(años, america_norte, color='blue', label='América del Norte')

# Ajuste de línea de regresión
coef_norte = np.polyfit(años, america_norte, 1)
polinomio_norte = np.poly1d(coef_norte)
plt.plot(años, polinomio_norte(años), color='black', label='Línea de regresión')

# Ecuación y coeficiente R²
r_squared_norte = np.corrcoef(años, america_norte)[0, 1]**2
plt.text(2016, 30, f"y = {coef_norte[0]:.2f}x + {coef_norte[1]:.2f}\nR² = {r_squared_norte:.2f}", fontsize=10)

# Configuración de la gráfica
plt.title("Crecimiento de la adopción de Edge Computing (América del Norte)")
plt.xlabel("Año")
plt.ylabel("Adopción (%)")
plt.grid(alpha=0.5)
plt.legend()
plt.tight_layout()

# Mostrar gráfica
plt.show()

#Hipótesis sobre el crecimiento de Edge Computing:
#Hipótesis: El crecimiento de Edge Computing está positivamente
# correlacionado con la expansión de tecnologías que demandan
# baja latencia y procesamiento descentralizado, como IoT, vehículos 
# autónomos y redes 5G. Esta adopción es impulsada por la necesidad 
# de manejar grandes volúmenes de datos en tiempo real, minimizando
# la dependencia de centros de datos centrales, especialmente en regiones
# con rápido desarrollo tecnológico como Asia y América del Norte.

#Argumentación:
#América del Norte lidera debido a su alta inversión en infraestructura tecnológica
# y adopción temprana de IoT y 5G.
#Asia muestra un crecimiento acelerado gracias a su fuerte apuesta por ciudades 
# inteligentes y manufactura avanzada.
#Europa mantiene un crecimiento constante, 
# influido por su enfoque en sostenibilidad y automatización industrial.
#Regiones como América Latina y África, aunque presentan cifras más bajas, 
# muestran un crecimiento gradual por la expansión de redes móviles y adopción tecnológica.