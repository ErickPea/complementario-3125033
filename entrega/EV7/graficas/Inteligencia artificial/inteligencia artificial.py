import matplotlib.pyplot as plt
import numpy as np

# Datos de adopción de IA y proyectos por región
adopcion_ia = [10, 12, 15, 18, 22, 25, 28, 30, 35]  # Porcentaje de adopción (2015-2023)
proyectos_activos = [100, 150, 250, 400, 500, 600, 650, 700, 800]  # Proyectos activos (en miles)

# Gráfica de dispersión
plt.figure(figsize=(8, 6))
plt.scatter(adopcion_ia, proyectos_activos, color='blue', label='Datos')

# Ajuste de línea de regresión
coef = np.polyfit(adopcion_ia, proyectos_activos, 1)
polinomio = np.poly1d(coef)
plt.plot(adopcion_ia, polinomio(adopcion_ia), color='black', label='Línea de regresión')

# Ecuación y coeficiente R²
r_squared = np.corrcoef(adopcion_ia, proyectos_activos)[0, 1]**2
plt.text(12, 700, f"y = {coef[0]:.2f}x + {coef[1]:.2f}\nR² = {r_squared:.2f}", fontsize=10)

# Configuración de la gráfica
plt.title("Correlación entre adopción de IA y proyectos activos")
plt.xlabel("Adopción de IA (%)")
plt.ylabel("Proyectos activos (en miles)")
plt.grid(alpha=0.5)
plt.legend()
plt.tight_layout()

# Mostrar gráfica
plt.show()
