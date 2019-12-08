def incident_edges(G, T):
    '''Function that looks for all edges connected to a vertices and makes sure they dont create a cycle 

    Parameters
    ----------
    G : tuple
        The graph extracted from users txt file using get_graph
    T : tuple
        Tuple containing a vertex and an empty list

    Returns
    -------
    list
        A list containing all incident edges, in respect to the current vertex
    '''
    edges = []
    for e in G[1]:
        for v in T[0]:
            if v in e and e not in T[1] and ((e[0] not in T[0]) or (e[1] not in T[0])):
                edges.append(e)
    return edges

def cost(G,e):
    '''Returns the cost of a certain edge e'''
    return G[1][e]