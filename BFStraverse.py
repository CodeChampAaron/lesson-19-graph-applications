#Breadth First Algorithm

import networkx as nx
import matplotlib.pyplot as plt

#Create empty networkx graph 
G = nx.DiGraph() 

#Add vertices of the graph
G.add_node("Castle") 
G.add_node("Village")
G.add_node("TownSquare") 
G.add_node("Market") 
G.add_node("Abbey") 
G.add_node("Monastery")
G.add_node("Cathedral") 
G.add_node("Church") 
G.add_node("Manor") 
G.add_node("Farmstead") 
G.add_node("Mill") 
G.add_node("Tavern") 
G.add_node("Blacksmith") 
G.add_node("Armory") 
G.add_node("Courtyard") 
G.add_node("GreatHall") 
G.add_node("Dungeon") 
G.add_node("Keep") 
G.add_node("WatchTower") 
G.add_node("MagicForest")
G.add_node("JoustingGrounds")  

#Add edges
G.add_edge("Castle", "Village")
G.add_edge("TownSquare", "Village")
G.add_edge("Castle", "TownSquare")
G.add_edge("Abbey", "Market")
G.add_edge("TownSquare", "Abbey")

G.add_edge("Castle", "GreatHall")
G.add_edge("TradingPost", "Market")
G.add_edge("Church", "Monastery")
G.add_edge("Courtyard", "Church")
G.add_edge("Church", "Cathedral")

G.add_edge("Courtyard", "Manor")
G.add_edge("Farmstead", "Mill")
G.add_edge("Mill", "Manor")
G.add_edge("Courtyard", "Tavern")
G.add_edge("Armory", "Blacksmith")

G.add_edge("GreatHall", "Blacksmith")
G.add_edge("Courtyard", "Armory")
G.add_edge("GreatHall", "Courtyard")
G.add_edge("Keep", "Dungeon")
G.add_edge("WatchTower", "MagicForest")
G.add_edge("Dungeon", "MagicForest")



G.add_edge("Monastery", "Keep")
G.add_edge("Blacksmith", "Church")
G.add_edge("Manor", "Cathedral")
G.add_edge("Market", "Tavern")
G.add_edge("Abbey", "Tavern")

G.add_edge("TownSquare", "TradingPost")
G.add_edge("Cathedral", "Monastery")
G.add_edge("TownSquare", "Courtyard")
G.add_edge("Manor", "Tavern")
G.add_edge("Abbey", "Keep")

G.add_edge("Manor", "Keep")
G.add_edge("Tavern", "Keep")
G.add_edge("Castle", "Farmstead")
G.add_edge("Tavern", "JoustingGrounds")
G.add_edge("JoustingGrounds", "Dungeon")

G.add_edge("Village", "Abbey")
G.add_edge("TradingPost", "JoustingGrounds")
G.add_edge("GreatHall", "Armory")
G.add_edge("Armory", "Manor")
G.add_edge("Keep", "WatchTower")

G.add_edge("Mill", "Monastery")
G.add_edge("Village", "Cathedral")
G.add_edge("Market", "JoustingGrounds")
G.add_edge("Farmstead", "Village")
G.add_edge("JoustingGrounds", "WatchTower")

G.add_edge("Blacksmith", "Cathedral")
G.add_edge("Tavern", "Monastery")


#Solution

# bfs_tree_edges = nx.bfs_edges(G, source = "Castle") 

# Visualize the graph and the minimum spanning tree

# pos = nx.spring_layout(G)
# nx.draw_networkx_nodes(G, pos, node_color="white", node_size=600)

# nx.draw_networkx_edges(G, pos, edge_color="black")
# nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")

# nx.draw_networkx_edges(G, pos, edgelist=list(bfs_tree_edges), edge_color="red", width=2)
# plt.axis("off")
# plt.show()

#mst_edges = bfs_tree_edges.edges()

#print(mst_edges)

# Perform BFS starting from nodes 1 and 3

bfs_medieval_edges1 = nx.descendants_at_distance(G, source="Castle", distance=1)
bfs_medieval_edges2 = nx.descendants_at_distance(G, source="Castle", distance=2)
bfs_medieval_edges3 = nx.descendants_at_distance(G, source="Castle", distance=3)
bfs_medieval_edges4 = nx.descendants_at_distance(G, source="Castle", distance=4)
bfs_medieval_edges5 = nx.descendants_at_distance(G, source="Castle", distance=5)

# Print the edges in the BFS forest

print("Distance: 1")
print(bfs_medieval_edges1)

print("Distance: 2")
print(bfs_medieval_edges2)

print("Distance: 3")
print(bfs_medieval_edges3)

print("Distance: 4")
print(bfs_medieval_edges4)

print("Distance: 5")
print(bfs_medieval_edges5)