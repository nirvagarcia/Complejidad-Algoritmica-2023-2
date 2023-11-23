import networkx as nx
import pandas as pd
import math
from enum import Enum


class errors(Enum):
    InternalServerError = -1
    NotFound = -2
    BadRequest = -3


print("Abriendo archivo...")
data = pd.read_csv('anime_data.csv', delimiter=";")
print("Inicializando atributos...")
attributes = [
    'titleEnglish'
    "titleRomaji",
    "startDate",
    "endDate",
    "format",
    "genres",
    "popularity",
    "score",
    "image"
]
Grafo = nx.Graph()
frontEndData = "[\n"
animeNames = []
animePictures = []
animeData = []
animeGenres = set()
print("Interpretando archivo...")
for index, row in data.iterrows():
    anime_title = row['titleEnglish']
    anime_attributes = {
        'titleEnglish': row['titleEnglish'],
        'titleRomaji': row['titleRomaji'],
        'startDate': row['startDate'],
        'endDate': row['endDate'],
        'format': row['format'],
        'genres': eval(row['genres']),
        'popularity': row['popularity'],
        'score': row['score'],
        'image': row['image']
    }

    animeData.append(anime_attributes)
    if type(anime_title) == float:
        anime_title = row['titleRomaji']
        anime_attributes['titleEnglish'] = row['titleRomaji']
    if math.isnan(anime_attributes['score']):
        anime_attributes['score'] = 0.0
    anime_attributes['name'] = anime_title
    for elements in anime_attributes['genres']:
        animeGenres.add(elements)
    Grafo.add_node(anime_title, **anime_attributes)
print("Resumiendo data...")
animeData = sorted(animeData, key=lambda x: x['name'])
for elements in animeData:
    animeNames.append(elements['name'])
    animePictures.append(elements['image'].replace("\\", "/"))
print("Calculando peso de las relaciones entre los nodos...")

def calcular_valor_relacion(anime1, anime2):
    generos_anime1 = set(Grafo.nodes[anime1]['genres'])
    generos_anime2 = set(Grafo.nodes[anime2]['genres'])
    generos_comunes = generos_anime1.intersection(generos_anime2)
    generos = generos_anime1.union(generos_anime2)
    popularidad_anime1 = Grafo.nodes[anime1]['popularity']
    popularidad_anime2 = Grafo.nodes[anime2]['popularity']
    diferencia_popularidad = abs(popularidad_anime1 - popularidad_anime2)
    sumapopularidad = popularidad_anime1 + popularidad_anime2
    valor_relacion = (len(generos) * 2 + (diferencia_popularidad / sumapopularidad)) * 4 / (
                1.1 + len(generos_comunes) * 3)
    if len(generos_comunes):
        return valor_relacion
    else:
        return 0


cantRelations = 0
for anime1 in Grafo.nodes:
    for anime2 in Grafo.nodes:
        if anime1 != anime2:
            valor_relacion = calcular_valor_relacion(anime1, anime2)
            if valor_relacion > 0:
                cantRelations += 1
                Grafo.add_edge(anime1, anime2, weight=valor_relacion)
print("Se han computado", cantRelations, "relaciones en total.")


def dijkstra(start, end):
    peso_final_del_camino = 0
    distancias = {}
    for node in Grafo.nodes:
        distancias[node] = math.inf
    if start in distancias and end in distancias:
        distancias[start] = 0
        camino_mas_corto = {}
        for node in Grafo.nodes:
            camino_mas_corto[node] = None

        nodos_no_visitados = list(Grafo.nodes)

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
            for vecino in Grafo.neighbors(nodo_actual):
                distancia_alternativa = distancias[nodo_actual] + Grafo[nodo_actual][vecino]['weight']

                if distancia_alternativa < distancias[vecino]:
                    distancias[vecino] = distancia_alternativa
                    camino_mas_corto[vecino] = nodo_actual
                    if vecino == end:
                        peso_final_del_camino = distancia_alternativa

    return None, peso_final_del_camino


def compute_relation(a, b):
    try:
        a = animeNames[int(a)]
        b = animeNames[int(b)]
        camino, peso = dijkstra(a, b)
        if camino:
            return {"result": round(-5.1 * peso + 100, 0)}
        else:
            return errors.NotFound
    except:
        return errors.InternalServerError
