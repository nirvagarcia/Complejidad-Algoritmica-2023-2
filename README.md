![image](https://github.com/nirvagarcia/Complejidad-Algoritmica-2023-2/blob/main/img/1.CaratulaLambers.png)

<br><br>
___
<br>


## Contenido

[1. Descripción del problema](1-Descripción-del-problema)
[2. Descripción y Visualización del conjunto de datos (dataset)](2-Descripción-y-Visualización-del-conjunto-de-datos-(dataset))
[3. Propuesta](3-Propuesta)
[4. Diseño del aplicativo](4-Diseño-del-aplicativo)
[5. Validación de resultados y pruebas](5-Validación-de-resultados-y-pruebas)
[6. Conclusiones](6-Conclusiones)
[7. Referencias bibliográficas](7-referencias-bibliográficas)

Repositorio de Github: https://github.com/nirvagarcia/Complejidad-Algoritmica-2023-2


<br><br>
___
<br>


# 1. Descripción del problema

Actualmente, la industria del entretenimiento ha experimentado un crecimiento significativo en la popularidad de los animes, y como prueba de esto, se ha observado que las personas que disfrutan de este contenido audiovisual japonés, han aumentado en un 37% alrededor del mundo en los últimos 5 años. (The Association of Japanese Animations, 2022).

Esta demanda ha llevado a un aumento en la cantidad de animes disponibles y plataformas de streaming que albergan este contenido, sin embargo, encontrar animes que se ajusten a las preferencias individuales de los usuarios puede resultar abrumador, debido a su amplia variedad de géneros. Según Ramu (2022), estima que el 70% de los fanáticos de anime emplean Internet y redes sociales como sus principales fuentes de recomendaciones, buscando opiniones y reseñas, pero las opiniones siempre son subjetivas y se basan en una decisión personal.

El problema que abordaremos es la dificultad de los usuarios para encontrar animes que sean de su agrado debido a la gran cantidad de opciones en el mercado actual. Nuestro objetivo principal es ofrecer a los usuarios una herramienta que les permita evaluar la probabilidad de que les guste un anime nuevo en función de su disfrute previo de otro anime específico. Esto tiene como finalidad evitar que los usuarios inviertan tiempo en ver animes que no se ajusten a sus gustos y preferencias, optimizando así su experiencia de entretenimiento.


<br><br>
___
<br>


# 2. Descripción y Visualización del conjunto de datos (dataset)

El conjunto de datos utilizado en este análisis se obtiene de la base de datos de AniDB (https://anidb.net/), una plataforma que almacena información detallada sobre diversas formas de animación asiática. Esta base de datos contiene información detallada de cada anime, pero los datos que extrajimos son: Title, Start date, End date, Format, Genres, Popularity, Score e Image.


Para esta extracción, generamos un programa con Python que nos permitió extraer el Dataset requerido de AniDB, generar un archivo CSV con toda esta data y, crear una carpeta que albergue las imágenes de portada de todos los animes analizados, también extraídas de AniDB. Este link muestra el código en Python realizado: 
https://github.com/nirvagarcia/Complejidad-Algoritmica-2023-2/blob/main/Data-Imgs-en-csv.py 

Mostramos la forma de nuestro Dataset, conformado por  7 columnas (los atributos del anime). En total, analizaremos 2000 animes (nodos).

|                 title                 |          startDate          |              endDate             |                      format                      |                       genres                      |                      popularity                      |                  score                 |                     image                     |
|:-------------------------------------:|:---------------------------:|:--------------------------------:|:------------------------------------------------:|:-------------------------------------------------:|:----------------------------------------------------:|:--------------------------------------:|:---------------------------------------------:|
| Nombre del anime, único en el dataset | Fecha de estreno del anime. | Fecha de finaliza ción del anime | Formato del anime (TV, Movie, ONA, OVA, Special) | Arreglo de géneros del anime (Drama, Acción, etc) | Número de personas que vieron el anime, según AniDB. | Puntua ción del anime en base a AniDB. | Imagen del anime para su aprecia ción visual. |


En nuestro diseño, utilizamos la librería NetworkX para representar internamente los nodos y sus conexiones en nuestro sistema de recomendación de anime. Cada nodo representa un anime y almacenamos su título como nombre del nodo, mientras que los datos del anime se almacenan en el cuerpo del nodo. Para establecer las conexiones entre los nodos, utilizamos la función add_edge de NetworkX. Esta función nos permite almacenar los nodos vecinos que tiene cada anime, lo que nos permite construir un grafo de conexiones entre los animes.

Para leer los datos del disco, utilizamos la función read_csv de la librería Pandas. Los datos se encontraban en un archivo .csv, donde estaban separados por punto y coma. Elegimos esta separación en lugar de comas debido a que dentro del archivo se almacenaban listas de géneros en formato de texto, representadas por valores entre corchetes separados por comas.

Para encontrar el camino mínimo que pudiera conectar dos animes y determinar qué tan diferentes eran, implementamos el algoritmo de Dijkstra. Este algoritmo fue elegido debido a que teníamos nodos conectados por pesos diferentes y queríamos encontrar el camino más corto entre ellos. Realizamos pruebas con diferentes casos dentro de nuestras posibilidades de datos y determinamos que el valor mínimo que podría devolver la función en caso de que los animes fueran idénticos en los valores evaluados era 2.2, mientras que el valor máximo era 19.4, lo que indicaría que los animes son muy diferentes.

Mostramos el código en Python realizado para generar el CSV de las conexiones entre animes: https://github.com/nirvagarcia/Complejidad-Algoritmica-2023-2/blob/main/Conexiones-Animes.py 


TTambién logramos generar una visualización del grafo de forma automática por código, usando la librería networkX, la cual genera imágenes como las siguientes, en las que se muestran los 2000 nodos y sus conexiones:
![Grafo SD Resolucion Reducida](https://github.com/nirvagarcia/Complejidad-Algoritmica-2023-2/blob/main/img/grafo%20reduct.png) 

Imagen 1: Visualización completa del Grafo

![Grafo HD Resolucion Reducida](https://github.com/nirvagarcia/Complejidad-Algoritmica-2023-2/blob/main/img/image%20(5).png)

Imagen 2: Visualización de realización de código del Grafo

![Grafo HD Resolucion Reducida](https://github.com/nirvagarcia/Complejidad-Algoritmica-2023-2/blob/main/img/sfdgsrgs.png)

Imagen 3: Visualización de cerca de los Nodos


Ambas son representaciones del mismo grafo, la diferencia entre ambas es el tamaño del lienzo usado. Como el lienzo del segundo es más grande, las aristas son más delgadas y los nodos están más separados En el segundo caso, usamos un lienzo 10 veces más grande que el primero, desafortunadamente, el espacio usado en memoria usado por el renderizador cuando el tamaño del lienzo es tan grande y el tiempo que demora en renderizarse hicieron que tuviéramos que configurar la aplicación para que genere el resto de representaciones con una menor resolución, como las que se observan en la imagen de la izquierda.


<br><br>
___
<br>


# 3. Propuesta

Nuestra propuesta consiste en desarrollar una aplicación web para calcular la similitud de dos animes elegidos por el usuario utilizando la técnica del Algoritmo de Dijkstra, que es una técnica de recorrido y búsqueda en grafos. El objetivo principal de esta propuesta es ayudar a aquellos fanáticos del anime de encontrar nuevas recomendaciones de anime en base a sus gustos actuales, ya que el gran catálogo de animes en la actualidad es muy extenso, dificultando el encontrar un buen anime que se adapte a tus gustos.

La aplicación consiste en una página en la que el usuario puede elegir dos animes, uno que ya ha visto, y uno que quiere ver. Tras seleccionar los animes, se calculará el camino mínimo entre estos, y en base al resultado del peso del camino, se calculara que tan probable es que al usuario le guste el segundo ánime, si le gustó el primero.

La elección de esta técnica se debe a su eficiencia y velocidad para encontrar la ruta más corta en un grafo ponderado. Según Association for Computing Machinery (2012), se demostró que el Algoritmo de Dijkstra puede ser aplicado exitosamente en sistemas de recomendación, permitiendo encontrar relaciones de similitud entre elementos y generar recomendaciones precisas. Implementaremos el Algoritmo de Dijkstra en nuestra aplicación web para encontrar el camino más corto entre dos animes dados, teniendo en cuenta la similitud de géneros y la popularidad que tienen en AniDB. Cada nodo en nuestro grafo representará un anime, y las conexiones entre los nodos representarán las relaciones entre géneros y audiencias similares.

Además, desarrollaremos la aplicación web utilizando el framework Flask, que es una opción sencilla y eficiente para proyectos de desarrollo web en Python. Flask proporciona una estructura flexible y fácil de usar, permitiéndonos implementar rápidamente la funcionalidad de nuestra aplicación web. Al combinar la potencia del Algoritmo de Dijkstra con la facilidad de desarrollo de Flask, lograremos una aplicación web que recomendará animes de manera precisa y eficiente, brindando a los usuarios una experiencia satisfactoria.



<br><br>
___
<br>


# 4. Diseño del aplicativo

Hemos decidido que el diseño del aplicativo sea de color negro ya que el color negro puede ayudar a resaltar los elementos visuales y el contenido del sitio de anime, permitiendo que las imágenes y los colores de los personajes y escenas sean el foco principal. Esto puede crear una atmósfera envolvente, atractiva y profesional para los usuarios, capturando la esencia del anime y brindando una experiencia visual inmersiva.

1). Comparador de Animes: Esta sección está compuesta por dos selectores de animes, y un knob que muestra el porcentaje de similitud entre estos dos, e instrucciones simples para el uso de la aplicación. El porcentaje de similitud y la lista de animes se obtienen del backend. El diseño de la aplicación usa colores oscuros para los fondos, y colores claros para el texto, para evitar causar fatiga visual. Los datos que se muestran por defecto son “imageNotFound.png” para las imágenes de los animes cuando aún no han sido elegidos, y “¡Elige un Anime!” en los selectores de texto.

![img 1](https://github.com/nirvagarcia/Complejidad-Algoritmica-2023-2/blob/main/img/parte%204%20imagen%201.jpg)

Imagen 4: Comparador de animes


![img 1](https://github.com/nirvagarcia/Complejidad-Algoritmica-2023-2/blob/main/img/imagen%20nueva%201.png)

Imagen 5: Comparador de animes


2). Selector de animes en texto: Este componente de la sección “Comparador de animes” permite a los usuarios elegir el anime que están buscando, de la lista de animes que tenemos en la base de datos. Este selector usa texto simple, por lo que puede cargar y mostrar todos los nombres de los animes disponibles fácilmente, sin suponer un consumo importante de backend. También muestra la carátula del anime seleccionado en grande tras elegir uno.


![img 1](https://github.com/nirvagarcia/Complejidad-Algoritmica-2023-2/blob/main/img/parte%204%20imagen%202.png)

Imagen 6: Diseño del selector de Animes, anime no seleccionado

![img 1](https://github.com/nirvagarcia/Complejidad-Algoritmica-2023-2/blob/main/img/parte%204%20imagen%203.png)


Imagen 7: Diseño del selector de Animes, anime seleccionado

3). Knob comparativo: El knob comparativo pertenece a la sección “Comparador de animes”, y es el encargado de mostrar el porcentaje de similitud entre los dos animes elegidos por el usuario. El valor por defecto que muestra es 0, si no se ha elegido ningún anime, o si no ha recibido el valor del backend.

![img 1](https://github.com/nirvagarcia/Complejidad-Algoritmica-2023-2/blob/main/img/parte%204%20imagen%204.png)

Imagen 8: Diseño del selector de Animes, anime seleccionado

![img 1](https://github.com/nirvagarcia/Complejidad-Algoritmica-2023-2/blob/main/img/imagen%20neuva%202.png)

Imagen 9: Diseño del selector de Animes, anime seleccionado

4). Selector de animes con portadas: En esta sección, se listan todos los animes existentes de la base de datos, con sus respectivas imágenes. Para ingresar a este selector, solo basta clickear la portada de uno de los dos animes en la pestaña principal. Este selector fue implementado en el componente Picker. Su función es facilitar al usuario encontrar un anime en concreto de forma más visual, para que pueda elegir uno de los dos animes a comparar. Este componente carga los animes usando Lazy Load, para no sobrecargar la base de datos o el servidor que provee las imágenes. Los animes mostrados se cargan de 10 en 10.

![img 1](https://github.com/nirvagarcia/Complejidad-Algoritmica-2023-2/blob/main/img/iamgen%20nueva%203.jpg)


Imagen 10: Diseño del selector de animes con interfaz visual completa y lazy load



<br><br>
___
<br>

# 5. Validación de resultados y pruebas

Comparador de Animes:
| Prueba                           	| Entrada/Input (Anime 1)                          	| Entrada/Input (Anime 2)                          	| Resultado de la prueba (Salida/Output)<br>(Porcentaje de recomendación resultante) 	| Interpretación de los resultados de la prueba                                                                                                                                           	|
|----------------------------------	|--------------------------------------------------	|--------------------------------------------------	|------------------------------------------------------------------------------------	|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| Animes con géneros diferentes    	| Teasing Master Takagi San<br>(Romance y Comedia) 	| Death Note<br>(Misterio, Psicológico y Thriller) 	| Resultado: 30%<br>[Imagen 9: Resultado de prueba]                                  	| Cuando se comparan animes con géneros diferentes, como Teasing Master Takagi-San (Romance y Comedia) con Death Note (Misterio, Psicológico y Thriller), el resultado es bajo (30%).     	|
| Animes con géneros identicos     	| Your Lie in April (Romance y Drama)              	| Given (Romance y Drama)                          	| Resultado: 87%<br>[Imagen 10: Resultado de prueba]                                 	| Cuando se comparan animes que tienen géneros idénticos, como Your Lie in April (Romance y Drama) y Given (Romance y Drama), el porcentaje de recomendación resultante es muy alto (87%) 	|
| Animes con géneros similares     	| Your Lie in April (Romance y Drama)              	| Teasing Master Takagi San<br>(Romance y Comedia) 	| Resultado: 69%<br>[Imagen 11: Resultado de prueba]                                 	| Cuando se comparten algunos géneros, como Teasing Master Takagi-San (Romance y Comedia), y Your Lie in April (Romance y Drama), el porcentaje de recomendación es alto (69%)            	|
| Animes con géneros muy similares 	| One Piece (Acción, Aventura y Fantasía)          	| Attack on Titan<br>(Acción, Drama y Fantasía)    	| Resultado: 75%<br>[Imagen 12: Resultado de prueba]                                 	| Cuando se comparten muchos géneros, como One Piece (Acción, Aventura y Fantasía), y Attack on Titan (Acción, Drama y Fantasía), la recomendación resultante es alta (75%)               	|


![img 1](https://github.com/nirvagarcia/Complejidad-Algoritmica-2023-2/blob/main/img/parte%206%20img%201.png)

Imagen 11: Resultado de prueba.

![img 1](https://github.com/nirvagarcia/Complejidad-Algoritmica-2023-2/blob/main/img/parte%206%20img%202.png)

Imagen 12: Resultado de prueba

![img 1](https://github.com/nirvagarcia/Complejidad-Algoritmica-2023-2/blob/main/img/parte%206%20img%203.png)

Imagen 13: Resultado de prueba

![img 1](https://github.com/nirvagarcia/Complejidad-Algoritmica-2023-2/blob/main/img/parte%206%20img%204.png)

Imagen 14: Resultado de prueba

Frontend: https://github.com/nirvagarcia/Complejidad-Algoritmica-2023-2/tree/6bdd8cf7d1e33c25cc4609ec63ffc33c8f459518/anime_comparator

Flask: https://github.com/nirvagarcia/Complejidad-Algoritmica-2023-2/blob/main/backend.py

Lógica en Python: https://github.com/nirvagarcia/Complejidad-Algoritmica-2023-2/blob/main/BackEndLogica.py

Base de datos: https://github.com/nirvagarcia/Complejidad-Algoritmica-2023-2/blob/main/anime_data.csv



<br><br>
___
<br>


# 6. Conclusiones 

En conclusión, nuestra aplicación web, basada en el Algoritmo de Dijkstra para calcular la similitud entre dos animes, representa una herramienta eficiente y sin complicaciones para los aficionados del anime que buscan descubrir nuevas opciones alineadas con sus gustos. Al permitir a los usuarios comparar dos animes y obtener resultados personalizados sin requerir información personal, la aplicación ofrece una experiencia enfocada en la búsqueda de contenido atractivo. Aunque el experimento actual ha demostrado la viabilidad y utilidad de la aplicación, futuras investigaciones podrían explorar mejoras adicionales en la precisión del algoritmo, así como la posibilidad de ampliar las funcionalidades para proporcionar una experiencia aún más enriquecedora a los usuarios.cado en diversos ámbitos del entretenimiento y la recomendación de contenido.




<br><br>
___
<br>



# 7. Referencias bibliográficas

AJA (2022). Anime Industry Report 2022. Recuperado de https://aja.gr.jp/download/2022 anime_ind_rpt_summary_en [Consulta: 10 de septiembre de 2023]

Association for Computing Machinery. (2012). The Proceedings of the 21st ACM International Conference on Information and Knowledge Management. Recuperado de https://dl.acm.org/action/showFmPdf?doi=10.1145%2F2396761 [Consulta: 10 de septiembre de 2023]

Ramu, P. (2022). Deep Learning-Based Anime and Movie Recommendation System (Doctoral dissertation, Dublin, National College of Ireland). Recuperado de https://norma.ncirl.ie/6280/  [Consulta: 10 de septiembre de 2023]
