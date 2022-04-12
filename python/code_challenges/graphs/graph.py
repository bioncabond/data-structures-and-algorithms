from code_challenges.stack_and_queue.queue import Queue

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, value):
        """
        add node
        Arguments: value
        Returns: The added node
        Add a node to the graph
        """
        v = Vertex(value)
        self.adjacency_list[v] = []
        return v

    def add_edge(self, start_vertex, end_vertex, weight=1):
        """
        add edges
        Arguments: 2 nodes to be connected by the edge, weight (optional)
        Returns: nothing
        Adds a new edge between two nodes in the graph
        If specified, assign a weight to the edge
        Both nodes should already be in the Graph
        """
        if start_vertex not in self.adjacency_list:
            raise KeyError("Starting Vertex outside of Graph")
        if end_vertex not in self.adjacency_list:
            raise KeyError("End Vertex outside of Graph")

        edge = Edge(end_vertex, weight)
        adjacencies = self.adjacency_list[start_vertex]
        adjacencies.append(edge)

    def get_nodes(self):
        """
        Arguments: none
        Returns all of the nodes in the graph as a
        collection (set, list, or similar)
        """
        if self.adjacency_list == {}:
            return None
        else:
            nodes = [*self.adjacency_list]
            print(nodes)

            for i in range(len(nodes)):
                nodes[i] = nodes[i].value

            return nodes

    def get_neighbor(self, node):
        """
        Arguments: node
        Returns a collection of edges connected to the given node
        Include the weight of the connection in the returned collection
        """
        nodes = [*self.adjacency_list]
        print(nodes)

        for i in range(len(nodes)):
            if nodes[i].value == node:
                adjacencies = self.adjacency_list[nodes[i]]
                print(adjacencies)

                adjacencies_with_weight = [
                    adjacencies[i].vertex.value,
                    adjacencies[i].weight,
                ]

                return adjacencies_with_weight
            else:
                raise KeyError("Null")

    def size(self):
        """
        size
        Arguments: none
        Returns the total number of nodes in the graph
        """
        return len(self.adjacency_list)

    def breadth_first(self, og_vertex):
        visited_vertices = []
        vertex_queue = Queue()
        i = 0
        for vertex in self.adjacency_list:
            if og_vertex == vertex.value:
                vertex_queue.enqueue(vertex)
                break
            i += 1
            if i == self.size():
                raise KeyError("Vertex outside of graph")

        j = 0
        while j < self.size() + 1:
            vertex = vertex_queue.dequeue()
            if vertex.value not in visited_vertices:
                visited_vertices.append(vertex.value)
                for neighbor in self.adjacency_list[vertex]:
                    vertex_queue.enqueue(neighbor.vertex)
            j += 1

        return visited_vertices

    def depth_first(self, og_vertex):
        visited_vertices = []
        known_neighbors = []
        og_vertex = Graph.vertex_converter(self, og_vertex)

        def traverse(vertex):
            visited_vertices.append(vertex.value)
            for neighbor in self.adjacency_list[vertex]:
                if neighbor.vertex not in known_neighbors and neighbor.vertex.value not in visited_vertices:
                    known_neighbors.append(neighbor.vertex)
                    traverse(neighbor.vertex)
                    known_neighbors.pop(-1)

        traverse(og_vertex)
        return visited_vertices

    @staticmethod
    def vertex_converter(self, selected_value):
        i = 0
        for vertex in self.adjacency_list:
            if vertex.value == selected_value:
                return vertex
            i += 1
            if i == self.size():
                raise KeyError("Vertex not in graph")


class Vertex:
    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, vertex, weight=1):
        self.vertex = vertex
        self.weight = weight
