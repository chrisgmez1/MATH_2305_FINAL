from functions.read_write_functions import get_graph

text = input ("Please provide a graph to run TSP on. ")
text = input ("Please provide a vertex. ")

T = prims(G,v)

print(f"Optimal tree is {T}")
