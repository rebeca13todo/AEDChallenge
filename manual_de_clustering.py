

''' INTRODUCCIÓN, ENTRADAS Y SALIDAS

El clustering es un proceso que recibe n puntos/observaciones/samples de d-dimensiones y los agupa según su parecido en k grupos. Cada grupo se 
llama "cluster" y tiene un "centroide" que representa una generalización de sus puntos, exactamente es la media de sus coordenadas. Puedes buscar 
más en internet: hay diversos tipos de clustering, cada uno con su casuística y es un rollo, así que no explico más. 

Nosotros usamos un algoritmo de cluster llamado KMeans. Las entradas y salidas del algoritmo son:

-> k (entrada) - Es un interger que representa la cantidad de centroides que se generarán.

-> Datos (entrada) - Es un dataframe que contiene las d coordenadas de los n puntos. En nuestro caso será una matriz de n*d. Si d=2, un cacho 
                      de esta matriz podría ser esto:

...
[27.03375    12.65875   ]
[25.417625   40.79175   ]
[10.531      16.535     ]
[29.3676     34.7904    ]
[ 5.0985     29.021     ]
[34.47128571 13.17828571]
[35.3994     44.786     ]
[ 2.404625   16.47425   ]
[26.81571429  5.14214286]
[14.78233333 23.497     ]
...

<- Coordenadas de los centroides (salida), es el atributo cluster_centers

<- A qué cluster pertenece cada sample (salida), es el atributo labels_

'''


'''Ahora vamos a hacer clustering. Partimos de que k=3 y tenemos estos datos bien organizados en una lista:'''

DATOS:list[tuple[float, float]] = [(24.412, 32.932), #Normalmente tendrás que acomodarte tú los datos de otro sitio
                                   (35.19, 12.189), 
                                   (26.288, 41.718), 
                                   (0.376, 15.506), 
                                   (26.116, 3.963), 
                                   (25.893, 31.515), 
                                   (23.606, 15.402), #Y sigue así para siempre....
                                   (28.026, 15.47), (26.36, 34.488), (23.013, 36.213), (27.819, 41.867), (39.634, 42.23), (35.477, 35.104), (25.768, 5.967), (-0.684, 21.105), (3.387, 17.81), (32.986, 3.412), (34.258, 9.931), (6.313, 29.426), (33.899, 37.535), (4.718, 12.125), (21.054, 5.067), (3.267, 21.911), (24.537, 38.822), (4.55, 16.179), (25.712, 7.409), (3.884, 28.616), (29.081, 34.539), (14.943, 23.263), (32.169, 45.421), (32.572, 16.944), (33.673, 13.163), (29.189, 13.226), (25.994, 34.444), (16.513, 23.396), (23.492, 11.142), (26.878, 36.609), (31.604, 36.911), (34.078, 33.827), (11.286, 16.082), (30.15, 9.642), (36.569, 45.827), (3.983, 11.839), (12.891, 23.832), (21.314, 13.264), (29.101, 44.781), (30.671, 9.294), (35.139, 9.803), (35.563, 42.759), (35.028, 15.779), (9.776, 16.988), (24.268, 5.693), (-0.36, 15.319), (33.062, 47.693), (21.034, 37.463), (31.806, 4.484), (22.493, 39.466), (29.056, 46.004), (29.822, 13.83), (35.439, 14.439)]

n = len(DATOS)
d = len(DATOS[0]) #d=2
k = 3


'''Lo primero que haremos será crear un objeto KMeans, que es quien tiene propiamente los métodos de clustering. Al inicializarlo, le 
pasamos que n_clusters=k. Para que clustee datos, tenemos que llamar a su función fit() y pasarle los datos. Lo hacemos directamente. 

DATO: En la función fit, puedes pasarle un argumento llamado sample_weight que es una lista de n floats donde cada elemento representa 
el peso del sample correspondiente. Si un sample tiene más peso, atraerá más a los centroides y tendrá más importancia.
'''

import sklearn.cluster
clusterizador = sklearn.cluster.KMeans( n_clusters=k )
clusterizador.fit( DATOS )


'''Ahora ya ha procesado los datos y hecho clustering. Finalmente, querríamos saber estas dos cosas:

-> Qué clusters se han hecho, dónde están los centroides: Para saber las coordenadas de los centroides consultamos el atributo  
   cluster_centers. Es una lista donde cada elemento es una lista con las coordenadas del cluster. Así: '''

print(clusterizador.cluster_centers_)

'''
[[ 6.32286667 19.5598    ] -> Coordenadas del primer cluster
 [29.30495652 39.05078261]  -> Coordenadas del segundo cluster
 [29.33086364 10.43240909]]  -> Coordenadas del tercer cluster

 
-> A qué cluster pertenece cada experimento: Consultamos el atributo labels_, que es una lista donde cada elemento es un interger que
   identifica al cluster en el que está el sample correspondiente. Los clusters se identifican por enteros 0, 1, 2, ... k-1. '''

print(clusterizador.labels_)
'''
[1, 2, 1, 0, 2, 1, 2, 2, 1, 1, 1, 1, 1, 2, 0, ... ] -> El primer sample pertenece al cluster 1, el segundo sample al 2, el tercero al 3, etc.
'''


'''Finalmente, este código dibuja los puntos y los samples: '''

import matplotlib.pyplot as plt
colores = ["red", "green", "blue", "yellow", "cyan", "magenta"] #Deben haber k colores o más

#Lista de las Xs e Ys de los samples y los clusters
samples_x:list[float] = [ p[0] for p in DATOS ]
samples_y:list[float] = [ p[1] for p in DATOS ]
clusters_x:list[float] = [p[0] for p in clusterizador.cluster_centers_ ]
clusters_y:list[float] = [p[1] for p in clusterizador.cluster_centers_ ]

#Dibujar los clusters grandes y claritos
plt.scatter( clusters_x, clusters_y, color="moccasin", marker='o', s=250)

#Dibujar los samples pequeños con un color distinto según el sample
for i in range(n):
   cluster = clusterizador.labels_[i]
   plt.scatter( samples_x[i], samples_y[i], color=colores[cluster], marker='o', s=5)

#Mostrar
plt.show()