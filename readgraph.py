import networkx as nx


def read_graph(file_path):
    new_graph = nx.Graph()
    with open(file_path, encoding='utf-8', mode="r") as f:
        for line in f:
            node1, node2, distance = line.split(' ')
            new_graph.add_edge(node1, node2, weight=int(distance))
    return new_graph
