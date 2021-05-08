#Create cvs reader to collect data on the number of unique stores, their country of operation, and the number of relationships they have

#initialize needed libraries
import csv
import os
from operator import itemgetter
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
from networkx.algorithms import community

#get file paths for edge and node data
raw_data = pd.read_csv('linked accounts.csv')

#fill blank cells with data
#raw_data.fillna("None",inplace = True)

#print(raw_data)

#format data so that we have a unique combination for each account and its respective connections
melted_data = raw_data.melt(['Account'],value_vars =['US','CANADA','MEXICO'],var_name = 'Source Company')
List_Remove = ["<<Presumably -- Insufficient Permissions>>","None", "<<Unknown>>","<<Presumably -- Store locked out>>","<<Unknown - store locked out>>"]

#print(melted_data)

#inplace = True replaces the previous value of the variable, default is False
melted_data.drop(melted_data[melted_data['value'].isin(List_Remove)].index, inplace = True) 

#cleaned_data = melted_d
# ata[melted_data['value' != "No Related Company"]]

#print(cleaned_data)

#runs networkx algo to create network matrix based off givine data, node source, target edge, with directional graphing
G = nx.from_pandas_edgelist(melted_data, source = "Account", edge_attr = True, target = "value", create_using=nx.DiGraph)

#Allow the user to choose what kind of network matrix they would like to create
userGraph = input("Choose a network matrix to draw: Circular, Network: ")
if userGraph == "Circular":
    nx.draw_circular(G,with_labels = True)

elif userGraph == "Network":
    nx.draw_networkx(G,with_labels = True)
else:
    nx.draw(G,with_labels = True)

#draws and displays graph using matplotlab
plt.draw()
plt.show()


###TO DO####

#As of now I am unsrue if all connections are shown, I need to find a way to drop the "No Related Comapny" Node
#Key companies with their respective country then group nodes by their country
#verify network accuracy