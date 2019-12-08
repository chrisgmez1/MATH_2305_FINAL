# Math 2305 Final: The Minimum Spanning Tree
#### by Christopher Gamez
## Terminology

### Graph:
A graph(G) is a pair of sets, namely a non-empty **vertex set**, V(G), and a set of **edges**, E(G), where each  
edge is a pair of vertices 
<img src = 'https://media.geeksforgeeks.org/wp-content/uploads/undirected-graph.jpg'>

(*Image from geeksforgeeks.com*)

In this diagram the vertices are {A,B,C,D,E,F} and the edges are {AB,AC,AF,BC,CD,CE,EF}
### Incident Edges:
Incident edges are edges connected to a certain vertex. For example, in the diagram the incident edges in regards to A are {AB,AC,AF}
### Trees:
Trees are graphs with no cycles.
### Cycle:
A cycles is a type of graph with a closed path.In a cycle a vertice.Below are examples of cycles.
<img src ='https://www.tutorialspoint.com/graph_theory/images/cycle_graph.jpg'>
(*Image from wolfram.com*)

## The Minimum Spanning Tree Problem: 
The objective of this project is to create an algorithm to find a subgraph whose total edge cost is minimized. We will be using **Prim's
Algorithm** to accomplish this.
Prim's Minimum Spanning Tree uses a starting vertex, typically chosen at random, and checks all incident edges connected to that vertex.
Then, you find the edge with the lowest value and you add the edge to the tree. You then repeat this using the other vertice on the edge
until all vertices are included within the tree as well as making sure no cycles are created when adding incident edges.

This program will ask the user to enter a graph you wish to run.If you wish to use your own graph make sure the graph 
is located within the Data folder in this project.

This program runs on Python and utilizes the NumPy package so make sure it is installed.
