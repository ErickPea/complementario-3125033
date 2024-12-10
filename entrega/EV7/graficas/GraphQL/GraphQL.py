import matplotlib.pyplot as plt
import numpy as np

# Datos
años = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])
america_norte = np.array([20, 25, 28, 30, 33, 35, 37, 40, 42])  # América del Norte (%)
asia = np.array([5, 7, 10, 12, 15, 18, 22, 25, 28])  # Asia (%)
europa = np.array([10, 12, 15, 18, 20, 22, 25, 28, 30])  # Europa (%)

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
plt.title("Crecimiento de la adopción de GraphQL (América del Norte)")
plt.xlabel("Año")
plt.ylabel("Adopción (%)")
plt.grid(alpha=0.5)
plt.legend()
plt.tight_layout()

# Mostrar gráfica
plt.show()
#Hipótesis: El crecimiento de GraphQL muestra una correlación positiva con el
# tiempo en todas las regiones debido a su creciente adopción en la comunidad de desarrolladores
# y empresas tecnológicas.
