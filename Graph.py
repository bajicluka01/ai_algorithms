class Node:
    def __init__(self, label, goal=False):
        self.label = label
        self.goal = goal
        self.neighbors = set()

    def is_goal(self):
        return self.goal
    
    def is_leaf(self):
        return len(self.neighbors) == 0
    
    def add_neighbor(self, neighbor):
        self.neighbors.add(neighbor)
        
class Edge:
    def __init__(self, u, v):
        self.u = u
        self.v = v

    def display(self):
        return f"({self.u.label}, {self.v.label})"

class Graph:
    def __init__(self, nodes, edges, directed = False):
        self.nodes = nodes
        self.edges = edges
        self.directed = directed
        self.add_neighbors()

    def add_neighbors(self):
        for edge in self.edges:
            self.nodes[edge.u.label].add_neighbor(edge.v.label)
            if not self.directed:
                self.nodes[edge.v.label].add_neighbor(edge.u.label)

    def is_leaf(self, node):
        if node not in self.nodes:
            return False
        
    def print(self):
        if self.directed:
            print("Directed graph:")
        else:
            print("Undirected graph:")
        print("Nodes: ")
        for label, node in self.nodes.items():
            if node.is_goal():
                print("\t", label, "(goal)")
            else:
                print("\t", label)
        
        print("Edges:")
        for edge in self.edges:
            print("\t", edge.display())
        
