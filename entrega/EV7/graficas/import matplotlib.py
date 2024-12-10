import matplotlib.pyplot as plt

# Datos
sistemas = ['Windows', 'macOS', 'Linux', 'Otro']
porcentajes = [61, 46, 45, 1]

# Crear el gráfico
plt.bar(sistemas, porcentajes, color=['blue', 'gray', 'green', 'red'])
plt.title('Uso de Sistemas Operativos')
plt.ylabel('Porcentaje (%)')
plt.xlabel('Sistema Operativo')

# Mostrar
plt.show()
