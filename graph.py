import networkx as nx
import csv
import matplotlib.pyplot as plt
G=nx.Graph()
with open("/Users/sujayr/PycharmProjects/covidfaketweets/Cleaned Twitter IDs - twitter_ids_cleaned.csv", newline='') as read_file:
    reader = csv.reader(read_file)
    rowNbr = 0
    for row in reader:
        if rowNbr >= 1 and row[6] != '':
            if row[6] in G.nodes():
                G.add_node(row[27])
                G.add_edge(row[6], row[27])
            else:
                G.add_node(row[6])
                G.add_node(row[27])
                G.add_edge(row[6], row[27])
        rowNbr = rowNbr + 1
print(G.edges())
nx.draw(G)
plt.show()