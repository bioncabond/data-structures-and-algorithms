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

    def business_trip(graph,cities):
        if graph.get_node() == None or cities == None:
            return False, 0

        cost = 0
        flight = False
        for i in range(0,len(cities) - 1):
            city = cities[i]
            neighbor = graph.adjacency_list[city]
            for edge in neighbor:
                if edge.vertex.value == cities[i + 1].value:
                    cost += edge.weight
                    flight = True
        return flight, f"${cost}"

class Vertex:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self, vertex,weight=1):
        self.vertex = vertex
        self.weight = weight

if __name__ == "__main__":
    graph = Graph()
    a = graph.add_node("a")
    b = graph.add_node("b")
    c = graph.add_node("c")
    graph.add_edge(a, b, 10)
    graph.add_edge(a, c, 345)
    flights = [a, c]
    print(graph.business_trip(flights))
