import matplotlib.pyplot as plt
import numpy as np
# Datos actualizados para Serverless Computing
years = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])
america_norte = np.array([22, 24, 27, 30, 33, 35, 37, 39, 41])  # América del Norte (%)
asia = np.array([8, 10, 13, 16, 20, 24, 27, 30, 34])  # Asia (%)
europa = np.array([12, 14, 17, 19, 21, 23, 25, 27, 29])  # Europa (%)

# Gráfica para América del Norte
plt.figure(figsize=(8, 6))
plt.scatter(years, america_norte, color='blue', label='América del Norte')

# Ajuste de línea de regresión
coef_norte = np.polyfit(years, america_norte, 1)
polinomio_norte = np.poly1d(coef_norte)
plt.plot(years, polinomio_norte(years), color='black', label='Línea de regresión')

# Ecuación y coeficiente R²
r_squared_norte = np.corrcoef(years, america_norte)[0, 1]**2
plt.text(2016, 30, f"y = {coef_norte[0]:.2f}x + {coef_norte[1]:.2f}\nR² = {r_squared_norte:.2f}", fontsize=10)

# Configuración de la gráfica
plt.title("Crecimiento de la adopción de Serverless Computing (América del Norte)")
plt.xlabel("Año")
plt.ylabel("Adopción (%)")
plt.grid(alpha=0.5)
plt.legend()
plt.tight_layout()

# Mostrar gráfica
plt.show()
#Hipótesis:
#El crecimiento de Serverless Computing tiene una correlación positiva con el
# tiempo en América del Norte, impulsado por el aumento en el uso de tecnologías como AWS Lambda,
# Google Cloud Functions y Azure Functions. Este crecimiento refleja la demanda de soluciones
# escalables y de bajo costo para aplicaciones modernas.