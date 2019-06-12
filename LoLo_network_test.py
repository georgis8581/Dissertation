
import pandas as pd

#inserting datasets
data = pd.read_excel (r'C:\Users\georg\Desktop\Data.xlsx', sheet_name='nodes')
df = pd.DataFrame (data, columns= ['node', 'demand'])
demand = df['demand'].tolist()

data1 = pd.read_excel (r'C:\Users\georg\Desktop\Data.xlsx', sheet_name='edges')
df1 = pd.DataFrame (data1, columns= ['origin', 'destination', 'weight'])

#setting edges characteristics
source = df1['origin'].tolist()
target = df1['destination'].tolist()
cost = df1['weight'].tolist()
links = []
for i in range(len(target)):
    links.append((source[i],target[i], cost[i]))

import networkx as nx 
#add nodes
G = nx.DiGraph()
G.add_nodes_from(nodes_for_adding=df['node'].tolist(), demand = demand)

#add edges
G.add_weighted_edges_from(links)

flowDict = nx.min_cost_flow(G)