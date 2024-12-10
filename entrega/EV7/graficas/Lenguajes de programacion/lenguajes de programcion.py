import matplotlib.pyplot as plt
import numpy as np

# Datos
regiones = ["Asia", "Europa", "América del Norte", "América Latina", "África", "Oceanía", "Otros"]
uso_porcentaje = [40, 34, 45, 32, 13, 8, 18]  # Porcentajes de 2023
num_desarrolladores = [300, 250, 400, 200, 50, 30, 70]  # Ejemplo ficticio (en miles)

# Gráfica de dispersión
plt.figure(figsize=(8, 6))
plt.scatter(uso_porcentaje, num_desarrolladores, color='blue', label='Datos')

# Ajuste de línea de regresión
coef = np.polyfit(uso_porcentaje, num_desarrolladores, 1)
polinomio = np.poly1d(coef)
plt.plot(uso_porcentaje, polinomio(uso_porcentaje), color='black', label='Línea de regresión')

# Ecuación y coeficiente R²
r_squared = np.corrcoef(uso_porcentaje, num_desarrolladores)[0, 1]**2
plt.text(10, 350, f"y = {coef[0]:.2f}x + {coef[1]:.2f}\nR² = {r_squared:.2f}", fontsize=10)

# Configuración de la gráfica
plt.title("Correlación entre uso de lenguajes de programación y desarrolladores")
plt.xlabel("Uso de lenguajes de programación (%)")
plt.ylabel("Número de desarrolladores (en miles)")
plt.grid(alpha=0.5)
plt.legend()
plt.tight_layout()

# Mostrar gráfica
plt.show()
#Hipótesis
#El crecimiento en la adopción de lenguajes como Python y TypeScript está altamente
#correlacionado con el aumento de proyectos de inteligencia artificial y desarrollo web
#moderno. Además, las tendencias demuestran que las regiones con economías tecnológicas más avanzadas 
#(América del Norte y Europa) adoptan lenguajes modernos más rápidamente, 
#mientras que las regiones emergentes tardan más en adaptarse a estas transiciones.