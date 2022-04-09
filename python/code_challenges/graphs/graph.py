from code_challenges.stack_and_queue.queue import Queue

class Graph:

    def __init__(self):
        self.adjacency_list = {}
    # key will be the node, value adj node with a value of the edge

    def add_node(self, value):
    # Arguments: value
    # Returns: The added node
    # Add a node to the graph or add to adj list
        v = Vertex(value)
        self.adjacency_list[v]=[]
        return v


    def add_edge(self,start_vertex,end_vertex,weight=1):
    # Arguments: 2 nodes to be connected by the edge, weight (optional)
    # Returns: nothing
    # Adds a new edge between two nodes in the graph
    # If specified, assign a weight to the edge
    # Both nodes should already be in the Graph
        if start_vertex not in self.adjacency_list:
            raise KeyError("You start vertex is broken.")
        if end_vertex not in self.adjacency_list:
            raise KeyError("You end vertex is broken.")

        edge = Edge(end_vertex,weight)
        adjacencies = self.adjacency_list[start_vertex]
        adjacencies.append(edge)

    def get_node(self):
    # Arguments: none
    # Returns all nodes in graph as a collection (set, list, or similar)
        if self.adjacency_list == {}:
            return None
        else:
            nodes = [*self.adjacency_list]
            print(nodes)

            for i in range(len(nodes)):
                nodes[i] = nodes[i].value
            return nodes


    def get_neighbor(self,node):
    # Arguments: node
    # Returns a collection of edges connected to the given node
    # Include the weight of connection in returned collection
        nodes = [*self.adjacency_list]
        print(nodes)

        for i in range(len(nodes)):
            if nodes[i].value == node:
                adjacencies = self.adjacency_list[nodes[i]]
                print(adjacencies)

                weight_adjacencies = [
                    adjacencies[i].vertex.value,
                    adjacencies[i].weight
                ]
                return weight_adjacencies
            else:
                raise KeyError("Null")

    def size(self):
    # Arguments: none
    # Returns the total number of nodes in the graph
        return len(self.adjacency_list)

    def breadth_first(self, origin_vertex):
        visited_vertices = []
        vertex_queue = Queue()
        i = 0
        for vertex in self.adjacency_list:
            if origin_vertex == vertex.value:
                vertex_queue.enqueue(vertex)
                break
            i += 1
            if i == self.size():
                raise KeyError("Vertex not in graph")

        j = 0
        while j < self.size() + 1:
            vertex = vertex_queue.dequeue()
            if vertex.value not in visited_vertices:
                visited_vertices.append(vertex.value)
                for neighbor in self.adjacency_list[vertex]:
                    vertex_queue.enqueue(neighbor.vertex)
            j += 1

        return visited_vertices

class Vertex:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self, vertex,weight=1):
        self.vertex = vertex
        self.weight = weight
