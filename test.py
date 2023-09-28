import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import math

Grafo = nx.Graph()

data = pd.read_csv('anime_data.csv', delimiter=";")

for index, row in data.iterrows():
    anime_title = row['titleEnglish']
    anime_attributes = {
        'titleRomaji': row['titleRomaji'],
        'startDate': row['startDate'],
        'endDate': row['endDate'],
        'format': row['format'],
        'genres': eval(row['genres']),
        'popularity': row['popularity'],
        'score': row['score'],
        'image': "/home/marcelo/documentation/" + row['image']
    }
    Grafo.add_node(anime_title, **anime_attributes)


def calcular_valor_relacion(anime1, anime2):
    generos_anime1 = set(Grafo.nodes[anime1]['genres'])
    generos_anime2 = set(Grafo.nodes[anime2]['genres'])
    generos_comunes = generos_anime1.intersection(generos_anime2)
    generos = generos_anime1.union(generos_anime2)
    popularidad_anime1 = Grafo.nodes[anime1]['popularity']
    popularidad_anime2 = Grafo.nodes[anime2]['popularity']
    diferencia_popularidad = abs(popularidad_anime1 - popularidad_anime2)
    sumapopularidad = popularidad_anime1 + popularidad_anime2
    valor_relacion = (len(generos)*2 + (diferencia_popularidad/sumapopularidad))*4 / (1.1 + len(generos_comunes)*3)
    if len(generos_comunes): return valor_relacion;
    else: return 0;

cantRelations = 0
for anime1 in Grafo.nodes:
    for anime2 in Grafo.nodes:
        if anime1 != anime2:
            valor_relacion = calcular_valor_relacion(anime1, anime2)
            if valor_relacion > 0:
                cantRelations += 1
                Grafo.add_edge(anime1, anime2, weight=valor_relacion)
print(cantRelations)

def dijkstra(graph, start, end):
    peso_final_del_camino = 0
    distancias = {}
    for node in graph.nodes:
        distancias[node] = math.inf
    if start in distancias and end in distancias:
        distancias[start] = 0
        camino_mas_corto = {};
        for node in graph.nodes:
            camino_mas_corto[node] = None

        nodos_no_visitados = list(graph.nodes)

        while nodos_no_visitados:
            nodo_actual = None
            distancia_minima = math.inf
            for node in nodos_no_visitados:
                if distancias[node] < distancia_minima:
                    nodo_actual = node
                    distancia_minima = distancias[node]

            # Si llegamos al nodo de destino, construye y devuelve el camino
            if nodo_actual == end:
                camino = []
                while nodo_actual is not None:
                    camino.insert(0, nodo_actual)
                    nodo_actual = camino_mas_corto[nodo_actual]
                return camino, peso_final_del_camino

            nodos_no_visitados.remove(nodo_actual)

            # Actualiza las distancias y los caminos para los nodos vecinos
            for vecino in graph.neighbors(nodo_actual):
                distancia_alternativa = distancias[nodo_actual] + graph[nodo_actual][vecino]['weight']

                if distancia_alternativa < distancias[vecino]:
                    distancias[vecino] = distancia_alternativa
                    camino_mas_corto[vecino] = nodo_actual
                    if vecino == end:
                        peso_final_del_camino = distancia_alternativa

    return None, peso_final_del_camino


def calcularDijkstra(a,b):
    camino, peso = dijkstra(Grafo, a, b)
    if camino:
        print(f"Ruta más corta entre {a} y {b}:")
        for node in camino:
            print(node)
        porcentajeRecomendacion = round(-5.64 * peso + 113.43,0)
        print(f"El porcentaje de recomendacion del anime {b} con respecto al anime {a} es del {porcentajeRecomendacion}%")
    else:
        print(f"No se encontró una ruta entre {a} y {b}. Posiblemente se deba a que {a} o {b} no esten en la base de datos.")

print("Para salir e imprimir el grafo en un archivo llamado grafo.png, escriba salir en cualquier input")
while(True):

    a = input("Ingrese el nombre del anime 1:")
    b = input("Ingrese el nombre del anime 2:")
    if a.lower() == "salir" or b.lower() == "salir":
        break
    else:
        calcularDijkstra(a, b)



layout_params = {
    'prog': 'neato',
    'args': '-Gscale=40.0',
}

A = nx.nx_agraph.to_agraph(Grafo)
A.layout(**layout_params)
A.draw('grafo.png')