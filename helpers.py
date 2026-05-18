from Graph import Node, Edge, Graph

def create_state_space(node_names, goal_nodes, edge_names, directed):
    nodes = {}
    for node in node_names:
        tmp = Node(node, node in goal_nodes)
        nodes[node] = tmp

    edges = []
    for edge in edge_names:
        edges.append(Edge(nodes[edge[0]], nodes[edge[1]]))

    G = Graph(nodes, edges, directed)
    return G
