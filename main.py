from functions.read_write_functions import get_graph
from functions.graph_functions import incident_edges, cost
from algorithms.prims_algorithm import prims,prims_cost

text =  (input(("Please provide a graph to run TSP on. ")))
G = get_graph(text)
text2 = (int(input("Please provide a vertex. ")))
v = ([text2],[])
T = prims(G,v)
sums = prims_cost(G,v)
print(f"Optimal tree is {T}")
print(f"Cost of optimal tree is {sums}")