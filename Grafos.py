#importamos la libreria de networkx y matplotlib
from turtle import pd
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

#importamos los datos para convertirlos en grafos
df = pd.read_csv(
    r"C:\Users\ACER PREDATOR\Desktop\universidad\Inteligencia artificial\buses_bucaramanga.csv"
)

#generamos la grafica a partir del dataframe con los datos    
BUSES = nx.from_pandas_edgelist(df, source='origen', target='destino', edge_attr='longitud_km')

#imprimimos los nodos y las aristas del grafo

print("NODOS:")
print(list(BUSES.nodes()))

print("ARISTAS:")
print(list(BUSES.edges()))

print("NUMERO DE NODOS:")
print(BUSES.order())

print("NUMERO DE ARISTAS:")
print(BUSES.size())

#estaciones a las que pertenece mas de 1 linea
print("ESTACIONES CON MAS DE UNA LINEA:")

#estaciones con mas de una linea
for node in BUSES.nodes():
    if BUSES.degree(node) > 2:
        print(f"Estacion: {node}, Lineas: {BUSES.degree(node)}")    


#implementamos el algoritmo de dijkstra para encontrar la ruta mas corta entre dos nodos
origen =  input("INGRESE LA ESTACION DE ORIGEN: ")
destino = input("INGRESE LA ESTACION DE DESTINO: ")
ruta_mas_corta = nx.dijkstra_path(BUSES, source=origen, target=destino, weight='longitud_km')
print(f"RUTA MAS CORTA ENTRE {origen} Y {destino}:")
print(ruta_mas_corta)

#dibujamos el grafo de la ruta mas corta
pos = nx.spring_layout(BUSES) #calcula una posición (x, y) para cada nodo del grafo BUSES usando un algoritmo de “resorte” (los nodos se repelen y las aristas actúan como resortes).
nx.draw(BUSES, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_size=10)
ruta_edges = list(zip(ruta_mas_corta, ruta_mas_corta[1:]))
nx.draw_networkx_edges(BUSES, pos, edgelist=ruta_edges, edge_color='red', width=2)
plt.title(f"Ruta mas corta entre {origen} y {destino}")
plt.show()  