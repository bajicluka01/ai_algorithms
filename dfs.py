from helpers import create_state_space
from Graph import Node, Edge, Graph

def dfs(state_space, start):
    print(state_space.nodes[start].label)

if __name__ == "__main__":
    nodes = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "m", "n", "p", "q"]
    goal_nodes = ["i", "n"]
    edges = [("a", "b"), ("a", "c"), ("a", "e"), ("a", "p"), ("b", "f"), ("b", "g"), ("c", "g"), ("c", "h"), ("c", "m"), ("e", "d"), ("p", "q"), ("p", "d"), ("d", "i"), ("i", "j"), ("j", "k"), ("k", "n")]
    state_space = create_state_space(nodes, goal_nodes, edges, True)
    state_space.print()

    dfs(state_space, "a")