from graph import AdjacentVertex
from graph import Graph

class Graph2(Graph):

    def min_number_edges(self, start: str, end: str) -> int:
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
            distances[v] = 100

        # The distance from origin to itself is 0
        distances[start] = 0
        if self._vertices[start] == []:
            for v in self._vertices.keys():
                distances[v] = 0
        else:

            for n in range(len(self._vertices)):

                # Seleccionamos el vertice mas cercano al vertice actual, con la condicion de que no se haya visitado
                # en la primera iteracion como origen no esta visitado y
                # la distancia del origen al vertice actual (que es origen) es 0 u sera = origin
                min = 100

                # buscamos cual es el vertice NO VISITADO mas cercano AL ORIGEN
                for vertex in self._vertices.keys():
                    if distances[vertex] <= min and visited[vertex] == False:
                        min = distances[vertex]  # update the new smallest
                        min_vertex = vertex  # update the index of the smallest
                u = min_vertex

                # marcamos el vertice actual como visitado para no volver a visitarlo
                visited[u] = True

                # vamos a recorrer los vertices adjacecentes al vertice actual u, para actualizar su distancia
                # al origen unicamente si la distancia actual es mayor que la nueva distancia
                for adj in self._vertices[u]:
                    i = adj.vertex
                    w = 1
                    if visited[i] == False and distances[i] > distances[u] + w:
                        # tenemos que comprobar que no esta visitado el vertice ya que si esta
                        # visitado no se actualiza la distancia para no dar vueltas en circulos

                        # actualizamos la distancia del vertice actual al origen
                        distances[i] = distances[u] + w
                        previous[i] = u

            # finally, we print the minimum path from origin to the other vertices
        return distances[end]

    def transpose(self) -> 'Graph2':
        """ returns a new graph that is the transpose graph of self"""
        g = Graph2(self._vertices.keys(), True)
        for i in self._vertices:
            for j in self._vertices[i]:
                g.add_edge(j.vertex, i, j.weight)

        return g

    def is_strongly_connected(self) -> bool:
        """ This function checks if the graph is strongly connected.
        A directed graph is strongly connected when for any
        pair of vertices u and v, there is always a path from u to v.
        If the graph is undirected, the function returns True if the graph is
        connected, that is, there is a path from any vertex to any other vertex
        in the graph.
        """
        vertices = []
        keys = []

        if not self._directed:
            for i in self._vertices.values():
                if len(i) == 1:
                    vecino = i[0].vertex
                    z = self._vertices[vecino]
                    if len(z) == 1:
                        return False

        for i in self._vertices.keys():
            keys.append(i)

        for j in self._vertices.values():
            for x in j:
                if x not in vertices:
                    vertices.append(x.vertex)
        for i in keys:
            if i not in vertices:
                return False
        return True



