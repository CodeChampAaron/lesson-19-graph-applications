
#A notorious witch lives in the town of Cisc, and she gives King Algo the creeps. The King is nervous that the Witch may poison the water supply,
#so he asked his most trustworthy Mathematician, Chatus Gptus to determine which roads would provide the quickest travel between the 
#castle and the witches hut, allowing the king's knights to swiftly deliever judgement should something suspicious occur. 
#
import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
G.add_node("Castle") 
G.add_node("WitchHut") 
G.add_node("FlowerShop") 
G.add_node("Piazza")
G.add_node("FarmersMarket") 
G.add_node("MysteryShack") 
G.add_node("Well") 
G.add_node("Guardpost1") 
G.add_node("Guardpost2") 
G.add_node("FishMarket") 
G.add_node("Cottage1") 
G.add_node("Cottage2") 
G.add_node("Cottage3") 
G.add_node("Cottage4") 
G.add_node("Cottage5") 
G.add_node("Cottage6") 
G.add_node("Cottage7") 
G.add_node("Cottage8") 
G.add_node("Cottage?") 
G.add_node("Observatory") 
G.add_node("Dock") 
G.add_node("Monastary") 
G.add_node("TradePost") 
G.add_node("Hospital") 
G.add_node("Saloon") 
G.add_node("Backrooms") 
G.add_node("School") 
G.add_node("Manor") 
G.add_node("Stables") 
G.add_edge("Castle", "Guardpost1", weight=3)
G.add_edge("Castle", "Guardpost2", weight=3)
G.add_edge("Castle", "Manor", weight=4)
G.add_edge("Manor", "Guardpost1", weight=2)
G.add_edge("Manor", "Guardpost2", weight=2)
G.add_edge("Guardpost1", "TradePost", weight=3)
G.add_edge("Guardpost2", "Stables", weight=1)
G.add_edge("Guardpost2", "TradePost", weight=3)
G.add_edge("Manor", "TradePost", weight=3)
G.add_edge("Stables", "TradePost", weight=1)
G.add_edge("TradePost", "FarmersMarket", weight=1)
G.add_edge("FarmersMarket", "FlowerShop", weight=1)
G.add_edge("FarmersMarket", "FishMarket", weight=1)
G.add_edge("FishMarket", "Dock", weight=2)
G.add_edge("Dock", "Saloon", weight=3)
G.add_edge("FarmersMarket", "Saloon", weight=2)
G.add_edge("FarmersMarket", "Well", weight=3)
G.add_edge("Saloon", "Well", weight=3)
G.add_edge("TradePost", "Well", weight=2)
G.add_edge("Monastary", "Well", weight=2)
G.add_edge("Monastary", "School", weight=2)
G.add_edge("Monastary", "Observatory", weight=6)
G.add_edge("School", "Cottage1", weight=1)
G.add_edge("Cottage2", "Cottage1", weight=7)
G.add_edge("School", "Cottage2", weight=1)
G.add_edge("Cottage1", "Cottage8", weight=3)
G.add_edge("Observatory", "Cottage8", weight=2)
G.add_edge("Monastary", "Cottage7", weight=8)
G.add_edge("Cottage8", "Cottage7", weight=1)
G.add_edge("Cottage7", "Cottage3", weight=1)
G.add_edge("Cottage7", "Cottage5", weight=1)
G.add_edge("Cottage3", "Well", weight=1)
G.add_edge("Cottage6", "Cottage7", weight=3)
G.add_edge("Cottage5", "Cottage6", weight=2)
G.add_edge("Cottage3", "Cottage4", weight=1)
G.add_edge("Cottage4", "Saloon", weight=1)
G.add_edge("Hospital", "Saloon", weight=2)
G.add_edge("Hospital", "Cottage5", weight=1)
G.add_edge("Cottage6", "Cottage?", weight=1)
G.add_edge("Cottage?", "MysteryShack", weight=9)
G.add_edge("MysteryShack", "WitchHut", weight=5)
G.add_edge("Cottage6", "Hospital", weight=1)
G.add_edge("Cottage5", "Cottage3", weight=1)
G.add_edge("Piazza", "School", weight=1)
G.add_edge("Piazza", "Observatory", weight=1)
G.add_edge("Piazza", "Cottage1", weight=1)
G.add_edge("Piazza", "Monastary", weight=1)














nx.draw(G,node_color = "green",with_labels=True, node_size= 300 )
plt.show()

#solution
print(nx.dijkstra_path(G, "Castle", "WitchHut", weight='weight'))
