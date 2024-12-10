import matplotlib.pyplot as plt
import numpy as np

# Datos
sistemas_operativos = ["Windows", "macOS", "Linux"]
uso_porcentaje = [61, 46, 45]  # Porcentaje de uso (%)
num_desarrolladores = [620, 310, 400]  # Número de desarrolladores 

# Gráfica de dispersión
plt.figure(figsize=(8, 6))
plt.scatter(uso_porcentaje, num_desarrolladores, color='blue', label='Datos')

# Ajuste de línea de regresión
coef = np.polyfit(uso_porcentaje, num_desarrolladores, 1)
polinomio = np.poly1d(coef)
plt.plot(uso_porcentaje, polinomio(uso_porcentaje), color='black', label='Línea de regresión')

# Ecuación y coeficiente R²
r_squared = np.corrcoef(uso_porcentaje, num_desarrolladores)[0, 1]**2
plt.text(30, 550, f"y = {coef[0]:.2f}x + {coef[1]:.2f}\nR² = {r_squared:.2f}", fontsize=10)

# Configuración de la gráfica
plt.title("Correlación entre uso de sistemas operativos y desarrolladores")
plt.xlabel("Uso de sistemas operativos (%)")
plt.ylabel("Número de desarrolladores (en miles)")
plt.grid(alpha=0.5)
plt.legend()
plt.tight_layout()

# Mostrar gráfica
plt.show()