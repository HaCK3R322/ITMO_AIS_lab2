from random import random
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.animation import FuncAnimation, PillowWriter


class SearchAnimation:
    def __init__(self, graph, visted_nodes, shortest_path, pause_time=2, interval=100, random_seed=53,
                 print_progress=False):
        self.graph = graph
        self.visted_nodes = visted_nodes
        self.shortest_path = shortest_path
        self.frames_number = len(visted_nodes) + len(shortest_path)
        self.interval = interval
        self.pause_frames = int(pause_time * 1000 / interval)
        self.node_colors_map = {node: "red" for node in graph}
        self.pos = nx.spring_layout(graph, seed=random_seed, scale=10)
        self.print_progress = print_progress

    def save(self, file_name):
        anim = FuncAnimation(plt.gcf(), func=self.update, interval=self.interval, frames=self.frames_number + self.pause_frames)
        anim.save(file_name, writer='pillow', dpi=300)

    def update(self, i):
        if self.print_progress:
            print(f"Rendered frame {i + 1}/{self.frames_number + self.pause_frames}")

        if i < self.frames_number:
            if i < len(self.visted_nodes):
                self.node_colors_map[self.visted_nodes[i]] = "blue"
            else:
                self.node_colors_map[self.shortest_path[i - len(self.visted_nodes)]] = "green"

        node_colors = [self.node_colors_map[node] for node in self.graph]

        plt.cla()
        nx.draw(self.graph, with_labels=True, node_color=node_colors, edge_color="black", font_color="black",
                pos=self.pos, font_size=8)
