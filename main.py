from random import random
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.animation import FuncAnimation, PillowWriter

from best_first_search import best_first_search
from bidirectional_search import bidirectional_search
from breadth_first_search import breadth_first_search
from depth_first_search import depth_first_search
from depth_limited_search import depth_limited_search
from iterative_deeping_search import iterative_deeping_search
from readgraph import read_graph
from search_a import search_a
from searchanim import SearchAnimation

# define number for nodes draw
MAGIC_NUMBER = 53
START_NODE = "Рига"
END_NODE = "Уфа"


G = read_graph("distances.txt")

# shortest_path, visited = breadth_first_search(G, START_NODE, END_NODE)
# anim = SearchAnimation(G, visited, shortest_path, print_progress=True)
# anim.save("animations/Поиск в ширину.gif")
#
# shortest_path, visited = depth_first_search(G, START_NODE, END_NODE)
# anim = SearchAnimation(G, visited, shortest_path, print_progress=True)
# anim.save("animations/Поиск в глубину.gif")
#
# shortest_path, visited = depth_limited_search(G, START_NODE, END_NODE, 1)
# anim = SearchAnimation(G, visited, shortest_path, print_progress=True)
# anim.save("animations/Поиск с ограничением глубины (глубина 1).gif")
#
# shortest_path, visited = depth_limited_search(G, START_NODE, END_NODE, 4)
# anim = SearchAnimation(G, visited, shortest_path, print_progress=True)
# anim.save("animations/Поиск с ограничением глубины (глубина 4).gif")
#
# shortest_path, visited = depth_limited_search(G, START_NODE, END_NODE, 10)
# anim = SearchAnimation(G, visited, shortest_path, print_progress=True)
# anim.save("animations/Поиск с ограничением глубины (глубина 10).gif")
#
# shortest_path, visited, final_depth = iterative_deeping_search(G, START_NODE, END_NODE)
# anim = SearchAnimation(G, visited, shortest_path, print_progress=True)
# anim.save(f"animations/Поиск с итеративным увеличением глубины (финальная глубина = {final_depth}).gif")
#
# shortest_path, visited = bidirectional_search(G, START_NODE, END_NODE)
# anim = SearchAnimation(G, visited, shortest_path, print_progress=True, interval=500)
# anim.save("animations/Двунаправленный поиск.gif")

# shortest_path, visited = best_first_search(G, START_NODE, END_NODE)
# anim = SearchAnimation(G, visited, shortest_path, print_progress=True)
# anim.save("animations/По наилучшему соответствию.gif")

shortest_path, visited = search_a(G, START_NODE, END_NODE)
anim = SearchAnimation(G, visited, shortest_path, print_progress=True)
anim.save("animations/A поиск.gif")