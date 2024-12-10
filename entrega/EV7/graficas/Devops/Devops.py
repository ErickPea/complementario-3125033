import matplotlib.pyplot as plt
import numpy as np

# Datos de adopción de DevOps (por región y años)
years = np.arange(2015, 2024)  # Años de 2015 a 2023

# Porcentajes de adopción por región (%)
asia = [10, 12, 14, 16, 18, 20, 22, 25, 28]
europa = [15, 17, 18, 20, 22, 24, 26, 28, 30]
america_norte = [25, 28, 30, 32, 35, 37, 38, 40, 42]
america_latina = [7, 9, 11, 12, 14, 15, 17, 18, 20]

# Crecimiento ficticio (en miles de proyectos/equipos adoptando DevOps)
proyectos_asia = [5, 8, 12, 18, 25, 30, 38, 45, 55]
proyectos_europa = [10, 14, 16, 20, 25, 30, 34, 40, 48]
proyectos_america_norte = [20, 30, 40, 50, 65, 75, 85, 95, 110]
proyectos_america_latina = [3, 5, 8, 12, 16, 20, 25, 28, 35]

# Gráfica de dispersión para América del Norte (como ejemplo principal)
plt.figure(figsize=(8, 6))
plt.scatter(america_norte, proyectos_america_norte, color='blue', label='Datos')

# Ajuste de línea de regresión para América del Norte
coef = np.polyfit(america_norte, proyectos_america_norte, 1)
polinomio = np.poly1d(coef)
plt.plot(america_norte, polinomio(america_norte), color='black', label='Línea de regresión')

# Ecuación y coeficiente R²
r_squared = np.corrcoef(america_norte, proyectos_america_norte)[0, 1]**2
plt.text(30, 100, f"y = {coef[0]:.2f}x + {coef[1]:.2f}\nR² = {r_squared:.2f}", fontsize=10)

# Configuración de la gráfica
plt.title("Correlación entre adopción de DevOps y proyectos (América del Norte)")
plt.xlabel("Adopción de DevOps (%)")
plt.ylabel("Número de proyectos/equipos (miles)")
plt.grid(alpha=0.5)
plt.legend()
plt.tight_layout()

# Mostrar gráfica
plt.show()
