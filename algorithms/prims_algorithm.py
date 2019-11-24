from functions.read_write_functions import get_graph
from functions.graph_functions import incident_edges, cost
def prims(G,v):
    while sorted(v[0])!=sorted(G[0]):
        min_val = 10000 # arbritrary number(can be replaced with any number, so long as its higher than any cost)
        edges = (incident_edges(G,v))
        for edge in edges:
            if cost(G,edge) <  min_val:
                min_val = cost(G,edge) 
                min_val_edge  = edge

        v[1].append(min_val_edge)

        for num in min_val_edge:
            if num not in v[0]:
                v[0].append(num)
    return v[1]

def prims_cost(G,v):
    T= prims(G,v)
    sums=0
    for sets in T:
        sums+= cost(G,sets)
    return sums
