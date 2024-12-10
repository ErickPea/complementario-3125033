import matplotlib.pyplot as plt
import numpy as np

# Datos para Arquitectura Hexagonal
years = np.arange(2015, 2024)
america_north = [15, 18, 20, 23, 25, 28, 30, 32, 35]

# Ajuste de regresión lineal
coefficients = np.polyfit(years, america_north, 1)
linear_fit = np.poly1d(coefficients)
r_squared = np.corrcoef(years, america_north)[0, 1]**2

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.plot(years, america_north, marker='o', label='Datos originales', color='blue')
plt.plot(years, linear_fit(years), label=f'Regresión lineal\n$y={coefficients[0]:.2f}x + {coefficients[1]:.2f}$\n$R^2={r_squared:.2f}$', linestyle='--', color='orange')

# Estilo y etiquetas
plt.title('Adopción de Arquitectura Hexagonal en América del Norte (2015-2023)', fontsize=14, fontweight='bold')
plt.xlabel('Año', fontsize=12)
plt.ylabel('Porcentaje de adopción (%)', fontsize=12)
plt.xticks(years, rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()

# Mostrar la gráfica
plt.show()
#import matplotlib.pyplot as plt
import numpy as np

# Datos para Arquitectura Hexagonal
years = np.arange(2015, 2024)
america_north = [15, 18, 20, 23, 25, 28, 30, 32, 35]

# Ajuste de regresión lineal
coefficients = np.polyfit(years, america_north, 1)
linear_fit = np.poly1d(coefficients)
r_squared = np.corrcoef(years, america_north)[0, 1]**2

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.plot(years, america_north, marker='o', label='Datos originales', color='blue')
plt.plot(years, linear_fit(years), label=f'Regresión lineal\n$y={coefficients[0]:.2f}x + {coefficients[1]:.2f}$\n$R^2={r_squared:.2f}$', linestyle='--', color='orange')

# Estilo y etiquetas
plt.title('Adopción de Arquitectura Hexagonal en América del Norte (2015-2023)', fontsize=14, fontweight='bold')
plt.xlabel('Año', fontsize=12)
plt.ylabel('Porcentaje de adopción (%)', fontsize=12)
plt.xticks(years, rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()

# Mostrar la gráfica
plt.show()
#import matplotlib.pyplot as plt
import numpy as np

# Datos para Arquitectura Hexagonal
years = np.arange(2015, 2024)
america_north = [15, 18, 20, 23, 25, 28, 30, 32, 35]

# Ajuste de regresión lineal
coefficients = np.polyfit(years, america_north, 1)
linear_fit = np.poly1d(coefficients)
r_squared = np.corrcoef(years, america_north)[0, 1]**2

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.plot(years, america_north, marker='o', label='Datos originales', color='blue')
plt.plot(years, linear_fit(years), label=f'Regresión lineal\n$y={coefficients[0]:.2f}x + {coefficients[1]:.2f}$\n$R^2={r_squared:.2f}$', linestyle='--', color='orange')

# Estilo y etiquetas
plt.title('Adopción de Arquitectura Hexagonal en América del Norte (2015-2023)', fontsize=14, fontweight='bold')
plt.xlabel('Año', fontsize=12)
plt.ylabel('Porcentaje de adopción (%)', fontsize=12)
plt.xticks(years, rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()

# Mostrar la gráfica
plt.show()


#Correlación: Existe una relación positiva fuerte entre los años y el porcentaje
# de adopción en América del Norte, con un 𝑅2R 2 alto, lo que indica que la tendencia 
#reciente está bien explicada por la regresión lineal.
#Hipótesis: A medida que las organizaciones buscan soluciones más escalables y modulares, 
# la adopción de la Arquitectura Hexagonal se ha incrementado consistentemente. Este crecimiento
# también podría estar relacionado con la proliferación de aplicaciones basadas en microservicios y 
# mejores prácticas de desarrollo en la región.
#
#