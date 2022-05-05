import sys

"""
GRAFOS:
un grafo puede contener cualquier tipo de conexión
los elementos de un grafo se llaman vertices y su conexion son aristas
Un grafo es ub conjunto de vertices(nodos) y aristas
Existen grafos no dirigidos, donde las aristas son bidireccionales y los grafos dirigidos, que la arista indica la direccion
Los grafos simples son los que tienen entre un origen y un destino solo una arista
las aaristas de un grafo van a ser n*(n-1) siendo n los vertices
Un grafo es escaso si el numero de sus aristas es cercano al de sus vertices
Un camino es una secuencia de vertices
Un camino simple es aquel que no repite vertices en su recorrido
Se implementará mediante una matriz de adyacencia y una lista de vertices
EJ:
[A,B,C,D,E,F] -->      [0 1 1 0 0 0]
 A ---- B ----E        [1 0 0 1 1 0]
 |      |__ D /        [1 0 0 0 0 1]
 |                     [0 1 0 0 1 0]
 C ---- F              [0 1 0 1 0 0]
                       [0 0 1 0 0 0]

Para hacer mas eficientes los grafos escasos, se pueden usar listas adyacentes
Se tiene una lista con los vertices y una lista con listas enlazadas
si es ponderado se mete un par
Tambien se pueden implementar con diccionarios de python {x:y}
class graph():
    def__...(self):
    self.vertex = {}
    ...
Ej
graph = {A: [B, C], B:[A, D, E]...}
cada clave es el vertice del grafo y su valor son los vertices adyacentes y la distancia

el algoritmo depth- first travel recorre el grafo hasta el final por un camino y despues vuelve atras para ir a otros
y asi sucesivamente hasta que haya recorrido el grafo


"""

# Matriz de adyacencia
class Graph():
    def __init__(self):
        self.vertex = {}


a = []
for item in range(3):
    a.append(item)
print(a)


class GraphDijkstra(Graph):

    def minDistance(self, distances, visited):
        """This functions returns the vertex (index) whose associated value in
        the dictionary distances is the smallest value. We
        only consider the set of vertices that have not been visited"""
        # la minima distancia sera infinito por defecto
        min = sys.maxsize

        # buscamos cual es el vertice NO VISITADO mas cercano AL ORIGEN
        for vertex in self._vertices.keys():
            if distances[vertex] <= min and visited[vertex] == False:
                min = distances[vertex]  # update the new smallest
                min_vertex = vertex  # update the index of the smallest

        return min_vertex

    def dijkstra(self, origin):
        """"This function takes a vertex v and calculates its mininum path
        to the rest of vertices by using the Dijkstra algoritm"""

        # visisted is a dictionary whose keys are the verticies of our graph.
        # When we visite a vertex, we must mark it as True.
        # Initially, all vertices are defined as False (not visited)
        visited = {}
        for v in self._vertices.keys():
            visited[v] = False

        # this dictionary will save the previous vertex for the key in the minimum path
        previous = {}
        for v in self._vertices.keys():
            # initially, we defines the previous vertex for any vertex as None
            previous[v] = None

        # This distance will save the accumulate distance from the
        # origin to the vertex (key)
        distances = {}
        for v in self._vertices.keys():
            distances[v] = sys.maxsize

        # The distance from origin to itself is 0
        distances[origin] = 0

        for n in range(len(self._vertices)):
            # Pick the vertex with the minimum distance vertex.
            # u is always equal to origin in first iteration

            # Seleccionamos el vertice mas cercano al vertice actual, con la condicion de que no se haya visitado
            # en la primera iteracion como origen no esta visitado y
            # la distancia del origen al vertice actual (que es origen) es 0 u sera = origin
            u = self.minDistance(distances, visited)

            # marcamos el vertice actual como visitado para no volver a visitarlo
            visited[u] = True

            # vamos a recorrer los vertices adjacecentes al vertice actual u, para actualizar su distancia
            # al origen unicamente si la distancia actual es mayor que la nueva distancia
            for adj in self._vertices[u]:
                i = adj._vertex
                w = adj._weight
                if visited[i] == False and distances[i] > distances[u] + w:
                    # tenemos que comprobar que no esta visitado el vertice ya que si esta
                    # visitado no se actualiza la distancia para no dar vueltas en circulos

                    # actualizamos la distancia del vertice actual al origen
                    distances[i] = distances[u] + w
                    previous[i] = u

        # finally, we print the minimum path from origin to the other vertices
        self.printSolution(distances, previous, origin)

    def printSolution(self, distances, previous, origin):
        print("Mininum path from ", origin)

        for i in self._vertices.keys():
            if distances[i] == sys.maxsize:
                print("There is not path from ", origin, ' to ', i)
            else:

                # minimum_path is the list wich contains the minimum path from origin to i
                minimum_path = []
                prev = previous[i]
                # this loop helps us to build the path
                while prev != None:
                    minimum_path.insert(0, prev)
                    prev = previous[prev]

                # we append the last vertex, which is i
                minimum_path.append(i)

                # we print the path from v to i and the distance
                print(origin, '->', i, ":", minimum_path, distances[i])

