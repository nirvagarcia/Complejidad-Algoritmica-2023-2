import pandas as pd
from sklearn.metrics.pairwise import euclidean_distances

# Cargar los datos desde el archivo CSV
data = pd.read_csv('anime.csv', delimiter=';')

# Crear un DataFrame para las conexiones
connections = {'source': [], 'target': []}

# Crear un diccionario para almacenar los géneros de cada anime
genre_dict = {}

# Construir el diccionario de géneros
for i, row in data.iterrows():
    genres = set(row['genres'].split(';'))
    genre_dict[row['id']] = genres

# Dividir los animes en grupos basados en géneros y puntuación
genre_groups = {}
for i, row in data.iterrows():
    genres = tuple(sorted(row['genres'].split(';')))
    score = row['score']
    key = (genres, score)
    if key not in genre_groups:
        genre_groups[key] = []
    genre_groups[key].append(row['id'])

# Iterar a través de los grupos y encontrar conexiones dentro de cada grupo
for group_animes in genre_groups.values():
    for i in range(len(group_animes)):
        for j in range(i + 1, len(group_animes)):
            # Comprobar si cumplen con las restricciones de puntuación
            score_i = data.loc[data['id'] == group_animes[i], 'score'].values[0]
            score_j = data.loc[data['id'] == group_animes[j], 'score'].values[0]
            score_difference = abs(score_i - score_j)
            
            if score_difference <= 10: 
                # Agregar la conexión al DataFrame
                connections['source'].append(group_animes[i])
                connections['target'].append(group_animes[j])

# Crear un DataFrame a partir del diccionario de conexiones
connections_df = pd.DataFrame(connections)

# Guardar las conexiones en un archivo CSV
connections_df.to_csv('anime_connections.csv', index=False)
