import osmnx as ox
import networkx as nx
from multiprocessing import Process
import matplotlib.pyplot as plt
# %matplotlib inline
ox.config(use_cache=True, cache_folder="cache")
ox.__version__

def f1(graph):
    print("f1")
    nc = ['b' if ox.is_endpoint(graph, node) else 'r' for node in graph.nodes()]
    figa, axa = ox.plot_graph(graph, node_color=nc, node_zorder=3)

def f2(G2):
    print("f2")
    loops = [edge[0] for edge in nx.selfloop_edges(G2)]
    nc = ['m' if node in loops else 'b' for node in G2.nodes()]
    figb, axb = ox.plot_graph(G2, node_color=nc, node_zorder=3)

def plot2(graph):
    p1 = Process(target=f1, args=(graph,))
    p1.start()

    # if __name__ == "__main__":
       #  thread = Thread(target = f1, args = (graph, ))
    G2 = graph.copy()
    G2 = ox.simplify_graph(G2)
    


    p2 = Process(target=f2, args=(G2,))
    p2.start()
    p1.join()
    p2.join()

def start():
    
    place_name = "Carvoeira, Florianopolis, Brazil"

    graph = ox.graph_from_place(place_name, simplify=False)
    print("downloaded")

    nodes = graph.nodes
    edges = graph.edges
    ma = graph.to_directed()

    # print(nodes)
    # print(edges)
    for x in graph.neighbors(1531132019):
        print(x)








    # type(graph)
    # nx.classes.multidigraph.MultiDiGraph


    # fig, ax = ox.plot_graph(graph)

    # plt.tight_layout()

    # nodes, edges = ox.graph_to_gdfs(graph)

    # return ox.graph_to_gdfs(graph)

start()
