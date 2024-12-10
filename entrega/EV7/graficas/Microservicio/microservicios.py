import matplotlib.pyplot as plt
import numpy as np

# Datos de adopción (nuevos ejes para dispersión)
adoption_percentage = [15, 20, 25, 30, 35, 40, 45, 50, 55]  # Promedios Asia, 2015-2023
dev_counts = [150, 200, 250, 300, 350, 400, 450, 500, 550]  # Desarrolladores hipotéticos (en miles)

# Gráfica de dispersión
plt.figure(figsize=(8, 6))
plt.scatter(adoption_percentage, dev_counts, color='blue', label='Datos')

# Línea de regresión
coefficients = np.polyfit(adoption_percentage, dev_counts, 1)
regression_line = np.poly1d(coefficients)
plt.plot(adoption_percentage, regression_line(adoption_percentage), color='black', label='Línea de regresión')

# Ecuación de regresión y coeficiente R²
r_squared_new = np.corrcoef(adoption_percentage, dev_counts)[0, 1] ** 2
plt.text(20, 500, f"y = {coefficients[0]:.2f}x + {coefficients[1]:.2f}\nR² = {r_squared_new:.2f}", fontsize=10)

# Configuración de la gráfica
plt.title("Correlación entre adopción de microservicios y desarrolladores")
plt.xlabel("Adopción de microservicios (%)")
plt.ylabel("Número de desarrolladores (en miles)")
plt.grid(alpha=0.5)
plt.legend()
plt.tight_layout()

# Mostrar gráfica
plt.show()
