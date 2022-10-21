# importing networkx
import networkx as nx
# importing matplotlib.pyplot
import matplotlib.pyplot as plt

G=nx.Graph()

G.add_node('A',pos=(0,2))
G.add_node('B',pos=(5,2))
G.add_node('C',pos=(1,3))
G.add_node('D',pos=(1,2))
G.add_node('E',pos=(1,0))
G.add_node('F',pos=(2,0))
G.add_node('G',pos=(4,1))
G.add_node('H',pos=(3,2))
G.add_node('I',pos=(2,3))

G.add_edge('A','C',weight=5)
G.add_edge('A','E',weight=2)
G.add_edge('A','D',weight=1)
G.add_edge('C','I',weight=2)
G.add_edge('C','D',weight=3)
G.add_edge('C','I',weight=2)
G.add_edge('I','H',weight=2)
G.add_edge('D','H',weight=2)
G.add_edge('H','B',weight=1)
G.add_edge('H','G',weight=2)
G.add_edge('G','B',weight=3)
G.add_edge('F','G',weight=1)
G.add_edge('E','F',weight=3)

pos=nx.get_node_attributes(G,'pos')
nx.draw(G,pos,with_labels = True)

labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels,font_size=15)

plt.savefig("filename.png")
print("terminé")


''' 
g = nx.Graph()
 
#g.add_edge(1, 2)
#g.add_edge(2, 3)
'''