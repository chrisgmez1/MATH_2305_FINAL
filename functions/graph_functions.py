def incident_edges(G, T):
    edges = []
    for e in G[1]:
        for v in T[0]:
            if v in e and e not in T[1] and ((e[0] not in T[0]) or (e[1] not in T[0])):
                edges.append(e)
    return edges

def cost(G,e):
    return G[1][e]