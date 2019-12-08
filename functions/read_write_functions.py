import numpy as np 
def get_graph(text_file):
    '''Functions that gets values from file and puts them in a tuple.

    Parameters
    ----------
    text_file:
        A text file used to read from
    
    Returns
    -------
    G
        A tuple containing a list of all vertices of the graph in G[0] and a dictionary with
        all edges and their respective values in G[1]
    '''

    edgelist = np.loadtxt(f"data\{text_file}",dtype =int)
    G =([],{})
    for x in edgelist:
        if x[0] not in G[0]:
            G[0].append(x[0])
        if x[1] not in G[0]:
            G[0].append(x[1])
        G[1][x[0], x[1]] =x[2]
    return G    