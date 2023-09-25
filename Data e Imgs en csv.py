import requests
import json
import csv
import os
import urllib.request
import time

#Primero definimos nuestra request como una cadena de varias lineas
queryIDs = '''
query($page: Int){
  Page(page: $page, perPage: 50) {
    media(type: ANIME) {
      id
    }
  }
}
'''

# Definimos las variables que serán usadas en la request
# Insertamos las variables en los argumentos del query
query = '''
query ($id: Int) { 
  Media (id: $id, type: ANIME) { 
    id
    title {
      romaji
      english
    }
    startDate {
      year
      month
      day
    }
    endDate {
      year
      month
      day
    }
    format
    genres
    averageScore
    popularity
    coverImage{
      large
    }
  }
}
'''

#  Ahora definimos nuestras variables de request y los valores que se utilizarán en la solicitud de request
url = 'https://graphql.anilist.co' #La DB de donde extraemos la data 
ids = []
animes = []
dif = 0
image_dir = "images"
if not os.path.exists(image_dir):
    os.makedirs(image_dir)


#Request donde pedimos ID de los primeros 2000 animes
page = 0
while(len(ids) < 2000):
    variables = {'page': page}
    response = requests.post(url, json={'query': queryIDs, 'variables': variables})
    parsedResponse = json.loads(response.content.decode());
    if(parsedResponse.get('errors')==None):
        for elements in parsedResponse['data']['Page']['media']:
            ids.append(elements['id'])
            print(ids[len(ids)-1],end=", ")
        page = page + 1
    else:
        print ("Falle, pipipi. ", parsedResponse['errors'])
        if(parsedResponse['errors'][0]['status'] == 429):
           print("Servidor saturado, esperando diez segundos...")
           time.sleep(10)
        else:
           page = page + 1

# Realizamos la HTTP Api request para cada anime
pos = 0
while True:
    if(pos >= len(ids)):
        break;
    variables = {'id': ids[pos]}
    response = requests.post(url, json={'query': query, 'variables': variables})
    parsedResponse = json.loads(response.content.decode());
    if(parsedResponse.get('errors')==None):
       animes.append(parsedResponse)
       print(parsedResponse)
       pos = pos +1
    else:
       print ("Falle, pipipi. ", parsedResponse['errors'])
       if(parsedResponse['errors'][0]['status'] == 429):
           print("Servidor saturado, esperando diez segundos")
           time.sleep(10)



#Generación del csv con los datos requeridos, y generación de un folder con las imagenes de los animes en cuestión
with open('anime2.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['titleEnglish', 'titleRomaji' ,'startDate', 'endDate', 'format', 'genres','popularity','score','image']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
    writer.writeheader()
    for anime in animes:
        anime = anime['data']['Media']
        titleEnglish = anime['title']['english']
        titleRomaji = anime['title']['romaji']
        startDate = str(anime['startDate']['day']) + "/" + str(anime['startDate']['month']) + "/" + str(anime['startDate']['year'])
        endDate = str(anime['endDate']['day']) + "/" + str(anime['endDate']['month']) + "/" + str(anime['endDate']['year'])
        emisionFormat = anime['format']
        genres = anime['genres']
        popularity = anime['popularity']
        averageScore = anime['averageScore']
        
        image_url = anime['coverImage']['large']
        image_path = ""
        if image_url is None:
            image_path = os.path.join(image_dir, 'noimage.png')
        else:
            image_path = os.path.join(image_dir, f'{anime["id"]}.png')
            os.system('wget -O \"' + image_path + '\" \"' + image_url + '\"')
        writer.writerow({'titleEnglish': titleEnglish, 'titleRomaji': titleRomaji,'startDate': startDate,'endDate': endDate, 'format': emisionFormat, 'genres': genres,'popularity': popularity, 'score': averageScore,'image':image_path})
