from functions.read_write_functions import get_graph
from functions.graph_functions import incident_edges, cost
def prims(G,v):
    ''' Prims algrithm used to find the minimum spanning tree

    Parameters
    ----------
    G : tuple
        The graph extracted from users txt file using get_graph
    v : tuple
        Tuple containing vertex chosen by user and an empty list

    Returns
    -------
    list
        The list of edges that make up the minimum spanning tree
    '''

    while sorted(v[0])!=sorted(G[0]):
        edges = (incident_edges(G,v))
        min_val = cost(G, edges[0])
        min_val_edge = edges[0]
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
    '''Function used to find the cost of the minimum spanning tree 

    Parameters
    ----------
    G:
        The graph extracted from users txt file using get_graph
    v:
        Vertex chosen by user
    
    Returns
    -------
    sums
        The sum of the values of all edges within the minimum spanning tree
    '''
    T= prims(G,v)
    sums=0
    for sets in T:
        sums+= cost(G,sets)
    return sums
