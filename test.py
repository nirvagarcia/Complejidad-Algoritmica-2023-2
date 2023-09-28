import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import math

Grafo = nx.Graph()

data = pd.read_csv('anime_data.csv', delimiter=";")


# print(data.head());

def calcular_valor_relacion(anime1, anime2):
    generos_anime1 = set(Grafo.nodes[anime1]['genres'])
    generos_anime2 = set(Grafo.nodes[anime2]['genres'])
    generos_comunes = generos_anime1.intersection(generos_anime2)
    valor_relacion = len(generos_comunes) >= (len(generos_anime2) + len(generos_anime1))/3
    return valor_relacion


def dijkstra(graph, start, end):
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
                return camino

            nodos_no_visitados.remove(nodo_actual)

            # Actualiza las distancias y los caminos para los nodos vecinos
            for vecino in graph.neighbors(nodo_actual):
                distancia_alternativa = distancias[nodo_actual] + graph[nodo_actual][vecino]['weight']
                if distancia_alternativa < distancias[vecino]:
                    distancias[vecino] = distancia_alternativa
                    camino_mas_corto[vecino] = nodo_actual

    return None


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

cantRelations = 0
for anime1 in Grafo.nodes:
    for anime2 in Grafo.nodes:
        if anime1 != anime2:
            valor_relacion = calcular_valor_relacion(anime1, anime2)
            if valor_relacion > 0.2:
                cantRelations += 1
                Grafo.add_edge(anime1, anime2, weight=valor_relacion)
print(cantRelations)

# animes para buscar
a = input("Ingrese el nombre del anime 1:")
b = input("Ingrese el nombre del anime 2:")

path = shortest_path = dijkstra(Grafo, a, b)

if shortest_path:
    print(f"Ruta más corta entre {a} y {b}:")
    for node in shortest_path:
        print(node)


else:
    print(f"No se encontró una ruta entre {a} y {b}.")

layout_params = {
    'prog': 'neato',
    'args': '-Gscale=40.0',
}

A = nx.nx_agraph.to_agraph(Grafo)
A.layout(**layout_params)
A.draw('salida3.png')