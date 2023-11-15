#Кодик
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, value):
        self.value = value
        self.parents = []
        self.children = []

def simplify(node, previous):
    global graph
    if len(node.parents) == 2:
        other_parent = [parent for parent in node.parents if parent != previous][0]
        other_parent.children.remove(node)
        for child in node.children:
            other_parent.children.append(child)
            child.parents.remove(node)
            child.parents.append(other_parent)

        graph.remove_node(node.value)
        del node

    else:
        for child in node.children:
            simplify(child, node)

def draw_graph(graph, title):
    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos)
    nx.draw_networkx_labels(graph, pos)
    nx.draw_networkx_edges(graph, pos, edgelist=graph.edges())
    plt.title(title)
    plt.show()

node_a = Node("A")
node_b = Node("B")
node_c = Node("C")
node_d = Node("D")
node_e = Node("E")

node_a.children = [node_b, node_c]
node_b.parents = [node_a]
node_c.parents = [node_a]

node_b.children = [node_d, node_e]
node_d.parents = [node_b, node_c]
node_e.parents = [node_b]

node_c.children = [node_d]
node_d.parents.append(node_c)

# Creating graphs
graph = nx.DiGraph()
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("B", "E")
graph.add_edge("C", "D")

draw_graph(graph, "Before Simplification")

simplify(node_a, None)

draw_graph(graph, "After Simplification")
