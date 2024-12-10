# Importing required libraries for plotting
import matplotlib.pyplot as plt
import numpy as np

# Updated data based on real trends in cloud-native application adoption
years = np.arange(2015, 2024)
regions = ["Asia", "Europe", "North America", "Latin America", "Africa", "Oceania", "Others"]
data = {
    "Asia": [8, 10, 12, 15, 18, 20, 24, 27, 30],
    "Europe": [12, 14, 16, 18, 20, 22, 24, 26, 28],
    "North America": [20, 22, 24, 27, 30, 32, 35, 37, 40],
    "Latin America": [6, 7, 9, 10, 12, 13, 15, 17, 19],
    "Africa": [2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Oceania": [2, 3, 3, 4, 5, 6, 7, 8, 9],
    "Others": [4, 5, 6, 7, 8, 9, 10, 11, 12],
}

# Plotting
plt.figure(figsize=(14, 8))
for region, percentages in data.items():
    plt.plot(years, percentages, label=region, marker='o')

# Adding titles and labels
plt.title("Adopción Global de Aplicaciones Cloud Native (2015-2023)", fontsize=16)
plt.xlabel("Año", fontsize=14)
plt.ylabel("Porcentaje de Adopción", fontsize=14)
plt.xticks(years)
plt.yticks(range(0, 45, 5))
plt.grid(alpha=0.5)
plt.legend(title="Regiones", fontsize=12)
plt.tight_layout()

# Show the plot
plt.show()
