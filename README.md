![image](https://github.com/nirvagarcia/Complejidad-Algoritmica-2023-2/blob/main/img/1.Caratula.png)

<br><br>
___
<br>


## Contenido

1. [Descripción del problema](#descripción-del-problema)
2. [Descripción y Visualización del conjunto de datos (dataset)](#descripción-y-visualización-del-conjunto-de-datos-dataset)
3. [Propuesta](#propuesta)
4. [Referencias bibliográficas](#referencias-bibliográficas)

<br><br>
___
<br>


## Descripción del problema

Actualmente, la industria del entretenimiento ha experimentado un crecimiento significativo en la popularidad de los animes, y como prueba de esto, se ha observado que las personas que disfrutan de este contenido audiovisual japonés, han aumentado en un 37% alrededor del mundo en los últimos 5 años. (The Association of Japanese Animations, 2022).

Esta demanda ha llevado a un aumento en la cantidad de animes disponibles y plataformas de streaming que albergan este contenido, sin embargo, encontrar animes que se ajusten a las preferencias individuales de los usuarios puede resultar abrumador, debido a su amplia variedad de géneros. Según Ramu (2022), estima que el 70% de los fanáticos de anime emplean Internet y redes sociales como sus principales fuentes de recomendaciones, buscando opiniones y reseñas, pero las opiniones siempre son subjetivas y se basan en una decisión personal.

El problema que abordaremos es la dificultad de los usuarios para encontrar animes que sean de su agrado debido a la gran cantidad de opciones en el mercado actual. El objetivo principal es proporcionar a los usuarios sugerencias de animes que se adapten a sus gustos y preferencias específicas, mejorando su experiencia de entretenimiento al permitirles descubrir nuevos animes que puedan disfrutar y evitar la frustración de tener que explorar un vasto catálogo sin guía.

<br><br>
___
<br>


## Descripción y Visualización del conjunto de datos (dataset)

Aquí va la descripción y visualización del conjunto de datos.

El conjunto de datos utilizado en este análisis se obtiene de la base de datos de AniDB (https://anidb.net/), una plataforma que almacena información detallada sobre diversas formas de animación asiática. Esta base de datos contiene información detallada de cada anime, pero los datos que extrajimos son: Main Title, Type, Year, Tags, Popularity, Score.

Para esta extracción, generamos un programa con Python que nos permitió extraer el Dataset requerido de AniDB, generar un archivo CSV con toda esta data y, crear una carpeta que albergue las imágenes de portada de todos los animes analizados, también extraídas de AniDB. Este link muestra el código en Python realizado: 

https://github.com/nirvagarcia/Complejidad-Algoritmica-2023-2/blob/main/Data-Imgs-en-csv.py 

Mostramos la forma de nuestro Dataset, conformado por  7 columnas (los atributos del anime). En total, analizaremos 1892 animes (nodos).

title
startDate
endDate
format
genres
popularity
score
image

Nombre del anime, único en el dataset
Fecha de estreno del anime.
Fecha de finaliza ción del anime
Formato del anime (TV, Movie, ONA, OVA, Special)
Arreglo de géneros del anime (Drama, Acción, etc)
Número de personas que vieron el anime, según AniDB.
Puntua ción del anime en base a AniDB.
Imagen del anime para su aprecia ción visual.


Ahora, en relación a las conexiones entre nodos, empleamos la estructura de Source y Target para indicar el punto de partida de una relación, y el punto final de la misma, además de añadir condicionales para obtener, en otro CSV, la conexión entre nuestro nodos a trabajar. Estas conexiones se construyen entre animes que cumplen con los criterios de géneros similares y una diferencia de puntuación aceptable (menor o igual a 10). Sin embargo, algunas de estas conexiones pueden ser duplicadas o redundantes,por lo que  el número de nodos únicos en el resultado es menor en comparación al de nuestro Dataset, el cuál ahora es de 1689 nodos. 

Mostramos el código en Python realizado para generar el CSV de las conexiones entre animes: https://github.com/nirvagarcia/Complejidad-Algoritmica-2023-2/blob/main/Conexiones-Animes.py 


Representamos lo mencionado anteriormente a través de un grafo generado por la herramienta de Gephi, logrando así, construir una representación gráfica comprensible de las relaciones entre los diferentes nodos de anime y sus conexiones. 


<br><br>
___
<br>


## Propuesta


Nuestra propuesta consiste en desarrollar una aplicación web para recomendar animes utilizando la técnica del Algoritmo de Dijkstra, que es una técnica de recorrido y búsqueda en grafos. La elección de utilizar esta metodología se debe a su eficiencia y capacidad para encontrar la ruta más corta en un grafo ponderado. Según Association for Computing Machinery (2012), se demostró que el Algoritmo de Dijkstra puede ser aplicado exitosamente en sistemas de recomendación, permitiendo encontrar relaciones de similitud entre elementos y generar recomendaciones precisas.

Implementaremos el Algoritmo de Dijkstra en nuestra aplicación web para encontrar el camino más corto entre los animes, teniendo en cuenta la similitud de género y la puntuación recogida en AniDB. Cada nodo en nuestro grafo representará un anime, y las conexiones entre los nodos representarán las relaciones entre géneros y puntuaciones similares.

Además, desarrollaremos la aplicación web utilizando el framework Flask, que es una opción sencilla y eficiente para proyectos de desarrollo web en Python. Flask proporciona una estructura flexible y fácil de usar, permitiéndonos implementar rápidamente la funcionalidad de nuestra aplicación web.

Al combinar la potencia del Algoritmo de Dijkstra con la facilidad de desarrollo de Flask, lograremos una aplicación web que recomendará animes de manera precisa y eficiente, brindando a los usuarios una experiencia satisfactoria.

<br><br>
___
<br>


## Referencias bibliográficas

AJA (2022). Anime Industry Report 2022. Recuperado de https://aja.gr.jp/download/2022 anime_ind_rpt_summary_en [Consulta: 10 de septiembre de 2023]

Association for Computing Machinery. (2012). The Proceedings of the 21st ACM International Conference on Information and Knowledge Management. Recuperado de https://dl.acm.org/action/showFmPdf?doi=10.1145%2F2396761 [Consulta: 10 de septiembre de 2023]

Ramu, P. (2022). Deep Learning-Based Anime and Movie Recommendation System (Doctoral dissertation, Dublin, National College of Ireland). Recuperado de https://norma.ncirl.ie/6280/  [Consulta: 10 de septiembre de 2023]
