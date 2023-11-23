import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import math

Grafo = nx.Graph()

data = pd.read_csv('anime_data.csv', delimiter=";")
#print(data.head());

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
        'image': row['image']
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


pos = nx.shell_layout(Grafo)
nx.draw(Grafo, pos, with_labels=False, node_size=10)
nx.draw_networkx_labels(Grafo, pos, font_size=6, font_color='r', font_family='sans-serif')

relaciones = [(anime1, anime2) for anime1, anime2, data in Grafo.edges(data=True)]
pesos = [data['weight'] for anime1, anime2, data in Grafo.edges(data=True)]
nx.draw_networkx_edges(Grafo, pos, edgelist=relaciones, width=pesos, edge_color='b')

plt.axis('off') 
plt.show()