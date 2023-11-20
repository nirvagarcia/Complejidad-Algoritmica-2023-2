![image](https://github.com/nirvagarcia/Complejidad-Algoritmica-2023-2/blob/main/img/1.CaratulaLambers.png)

<br><br>
___
<br>


## Contenido

1. [Descripción del problema](#descripción-del-problema)
2. [Descripción y Visualización del conjunto de datos (dataset)](#descripción-y-visualización-del-conjunto-de-datos-dataset)
3. [Propuesta](#propuesta)
4. [Referencias bibliográficas](#referencias-bibliográficas)


Repositorio de Github: https://github.com/nirvagarcia/Complejidad-Algoritmica-2023-2


<br><br>
___
<br>


## Descripción del problema

Actualmente, la industria del entretenimiento ha experimentado un crecimiento significativo en la popularidad de los animes, y como prueba de esto, se ha observado que las personas que disfrutan de este contenido audiovisual japonés, han aumentado en un 37% alrededor del mundo en los últimos 5 años. (The Association of Japanese Animations, 2022).

Esta demanda ha llevado a un aumento en la cantidad de animes disponibles y plataformas de streaming que albergan este contenido, sin embargo, encontrar animes que se ajusten a las preferencias individuales de los usuarios puede resultar abrumador, debido a su amplia variedad de géneros. Según Ramu (2022), estima que el 70% de los fanáticos de anime emplean Internet y redes sociales como sus principales fuentes de recomendaciones, buscando opiniones y reseñas, pero las opiniones siempre son subjetivas y se basan en una decisión personal.

El problema que abordaremos es la dificultad de los usuarios para encontrar animes que sean de su agrado debido a la gran cantidad de opciones en el mercado actual. Nuestro objetivo principal es ofrecer a los usuarios una herramienta que les permita evaluar la probabilidad de que les guste un anime nuevo en función de su disfrute previo de otro anime específico. Esto tiene como finalidad evitar que los usuarios inviertan tiempo en ver animes que no se ajusten a sus gustos y preferencias, optimizando así su experiencia de entretenimiento.

<br><br>
___
<br>


## Descripción y Visualización del conjunto de datos (dataset)

El conjunto de datos utilizado en este análisis se obtiene de la base de datos de AniDB (https://anidb.net/), una plataforma que almacena información detallada sobre diversas formas de animación asiática. Esta base de datos contiene información detallada de cada anime, pero los datos que extrajimos son: Title, Start date, End date, Format, Genres, Popularity, Score e Image.

Para esta extracción, generamos un programa con Python que nos permitió extraer el Dataset requerido de AniDB, generar un archivo CSV con toda esta data y, crear una carpeta que albergue las imágenes de portada de todos los animes analizados, también extraídas de AniDB. Este link muestra el código en Python realizado: 
https://github.com/nirvagarcia/Complejidad-Algoritmica-2023-2/blob/main/Data-Imgs-en-csv.py 

Mostramos la forma de nuestro Dataset, conformado por  7 columnas (los atributos del anime). En total, analizaremos 2000 animes (nodos).
|                 title                 |          startDate          |              endDate             |                      format                      |                       genres                      |                      popularity                      |                  score                 |                     image                     |
|:-------------------------------------:|:---------------------------:|:--------------------------------:|:------------------------------------------------:|:-------------------------------------------------:|:----------------------------------------------------:|:--------------------------------------:|:---------------------------------------------:|
| Nombre del anime, único en el dataset | Fecha de estreno del anime. | Fecha de finaliza ción del anime | Formato del anime (TV, Movie, ONA, OVA, Special) | Arreglo de géneros del anime (Drama, Acción, etc) | Número de personas que vieron el anime, según AniDB. | Puntua ción del anime en base a AniDB. | Imagen del anime para su aprecia ción visual. |


Para las conexiones entre nodos, utilizamos la librería NetworkX, únicamente para la representación interna de los nodos. En ellos, almacenamos el título del anime como nombre del nodo, y los datos del anime como cuerpo del nodo. Para la representación de las conexiones de los nodos, utilizamos la función add_edge, que nos permite almacenar los nodos vecinos que tiene cada nodo. Para la lectura de datos del disco utilizamos la función read_csv, que viene incluida en la librería Pandas. Los datos fueron leídos de un archivo .csv (Comma Separated Values), que tenía los datos separados por punto y coma. Elegimos separar los valores usando punto y coma en lugar de comas debido a que en el interior del archivo csv, se almacenan listas de python para guardar la lista de géneros que tiene cada anime, cuya representación en texto es una lista de valores entre corchetes separados por comas.

La conexión entre los nodos se hizo utilizando una función que evalúa la cantidad de géneros que cada anime tiene en común con otro anime, en relación al total de géneros que poseen, y la diferencia de popularidad entre ellos. La función fue diseñada para devolver un valor pequeño si los animes eran parecidos, y un valor grande si los animes eran muy diferentes. También evalúa si es que los animes tienen algún género en común. Si no tienen ninguno, entonces no se realiza una conexión.

El algoritmo que elegimos implementar fue Dijkstra, ya que teníamos nodos conectados por pesos diferentes, y queríamos hallar el camino mínimo que pudiera conectar dos animes, para saber qué tan diferentes son. Según las pruebas que realizamos manipulando los datos para el peor y el mejor caso dentro de las posibilidades de nuestro dataset, el valor del camino más corto que podría devolver la función en caso los animes sean idénticos en los valores evaluados, es 2.2, y el valor máximo que podría devolver la función es 19.4, que indicaría que los animes son muy diferentes.

Mostramos el código en Python realizado para generar el CSV de las conexiones entre animes: https://github.com/nirvagarcia/Complejidad-Algoritmica-2023-2/blob/main/Conexiones-Animes.py 

También logramos generar una visualización del grafo de forma automática por código, usando la libería networkX, la cual genera imágenes como las siguietes, en las que se muestran los 2000 nodos y sus conexiones:
![Grafo SD Resolucion Reducida](https://github.com/nirvagarcia/Complejidad-Algoritmica-2023-2/blob/main/img/grafo%20reduct.png) ![Grafo HD Resolucion Reducida](https://github.com/nirvagarcia/Complejidad-Algoritmica-2023-2/blob/main/img/grafoSD.png)
Ambas son representaciones del mismo grafo, la diferencia entre ambas es el tamaño del lienzo usado. Como el lienzo del segundo es más grande, las aristas son más delgadas y los nodos están más separados En el segundo caso, usamos un lienzo 10 veces más grande que el primero, desafortunadamente, el espacio usado en memoria usado por el renderizador cuando el tamaño del lienzo es tan grande y el tiempo que demora en renderizarse hicieron que tuviéramos que configurar la aplicación para que genere el resto de representaciones con una menor resolución, como las que se observan en la imagen de la izquierda.

Finalmente, creamos una función que se ejecuta en un bucle infinito y le solicita al usuario dos animes para comparar. 
![Grafo HD Resolucion Reducida](https://github.com/nirvagarcia/Complejidad-Algoritmica-2023-2/blob/main/img/Todo%20Funciona.png)
Como se observa en los resultados, cuando se comparan animes que tienen géneros parecidos, como Your Lie in April (Romance y Drama principalmente) y Given (Romance y Drama principalmente), el resultado es un porcentaje de recomendación muy alto (87%). Cuando se comparten algunos generos, como Teasing Master Takagi-San (Romance y Comedia), y Your Lie in April (Romance y Drama), el porcentaje de recomendación es alto (70%), pero cuando se comparan animes con géneros diferentes, como Teasing Master Takagi-San (Romance y Comedia) con Death Note (Misterio, Psicológico y Thriller), el resultado es bajo (30%).

Los porcentajes se generan con una función lineal matemática simple que convierte los resultados de los mínimos y máximos que devuelve el algoritmo de búsqueda a un nuevo mínimo y máximo (0 a 100).
<br><br>
___
<br>


## Propuesta

Nuestra propuesta consiste en desarrollar una aplicación web para calcular la similitud de dos animes utilizando la técnica del Algoritmo de Dijkstra, que es una técnica de recorrido y búsqueda en grafos. La elección de esta técnica se debe a su eficiencia y velocidad para encontrar la ruta más corta en un grafo ponderado. Según Association for Computing Machinery (2012), se demostró que el Algoritmo de Dijkstra puede ser aplicado exitosamente en sistemas de recomendación, permitiendo encontrar relaciones de similitud entre elementos y generar recomendaciones precisas.

Implementaremos el Algoritmo de Dijkstra en nuestra aplicación web para encontrar el camino más corto entre dos animes dados, teniendo en cuenta la similitud de géneros y la popularidad que tienen en AniDB. Cada nodo en nuestro grafo representará un anime, y las conexiones entre los nodos representarán las relaciones entre géneros y audiencias similares.

Además, desarrollaremos la aplicación web utilizando el framework Flask, que es una opción sencilla y eficiente para proyectos de desarrollo web en Python. Flask proporciona una estructura flexible y fácil de usar, permitiéndonos implementar rápidamente la funcionalidad de nuestra aplicación web.

Al combinar la potencia del Algoritmo de Dijkstra con la facilidad de desarrollo de Flask, lograremos una aplicación web que recomendará animes de manera precisa y eficiente, brindando a los usuarios una experiencia satisfactoria.

<br><br>
___
<br>


## Referencias bibliográficas

AJA (2022). Anime Industry Report 2022. Recuperado de https://aja.gr.jp/download/2022 anime_ind_rpt_summary_en [Consulta: 10 de septiembre de 2023]

Association for Computing Machinery. (2012). The Proceedings of the 21st ACM International Conference on Information and Knowledge Management. Recuperado de https://dl.acm.org/action/showFmPdf?doi=10.1145%2F2396761 [Consulta: 10 de septiembre de 2023]

Ramu, P. (2022). Deep Learning-Based Anime and Movie Recommendation System (Doctoral dissertation, Dublin, National College of Ireland). Recuperado de https://norma.ncirl.ie/6280/  [Consulta: 10 de septiembre de 2023]
