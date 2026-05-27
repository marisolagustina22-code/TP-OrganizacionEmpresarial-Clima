import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
datos = pd.read_csv("datos/dataset.csv")

# Indicadores climáticos
print("Temperatura promedio:", datos["temperatura"].mean())
print("Temperatura máxima:", datos["temperatura"].max())
print("Temperatura mínima:", datos["temperatura"].min())
print("Precipitación promedio:", datos["precipitacion"].mean())

# Gráfico de temperatura
plt.plot(datos["fecha"], datos["temperatura"])
plt.title("Evolución de la temperatura")
plt.xlabel("Fecha")
plt.ylabel("Temperatura")
plt.savefig("resultados/grafico_temperatura.png")
