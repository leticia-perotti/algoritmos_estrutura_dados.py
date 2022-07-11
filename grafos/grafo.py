import encodings
import networkx as nx
import pylab

G = nx.Graph()

G.add_node(1)
G.add_node(2)

#print(G.nodes())

G.add_edge(1,2)

nVertices = G.number_of_nodes()
nArestras = G.number_of_edges()

print(nVertices, nArestras)

G.add_edge(4,5)

#nx.draw(G)
#pylab.show()

#nx.draw(G, with_labels= True)
#pylab.show()

#nx.draw(G, with_labels= True, node_size= 1200, node_color = 'red')
#pylab.show()

subgrafos = [G.subgraph(s) for s in nx.connected_components(G)]
print(len(subgrafos))

'''
nx.draw(subgrafos[0],
        with_labels= True, 
        node_size= 800, 
        node_color = 'red')

nx.draw(subgrafos[1],
        with_labels= True, 
        node_size= 800, 
        node_color = 'blue')

pylab.show()
'''

nx.draw_circular(subgrafos[0],
        with_labels= True, 
        node_size= 800, 
        node_color = 'red')

nx.draw_random(subgrafos[1],
        with_labels= True, 
        node_size= 800, 
        node_color = 'blue')

pylab.show()

nx.write_edgelist(
    G,
    "grafos.csv",
    delimiter = ",",
    data = False,
    encoding = 'utf-8'
)