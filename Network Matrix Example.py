#Create cvs reader to collect data on the number of unique stores, their country of operation, and the number of relationships they have

#initialize needed libraries
import csv
import os
from operator import itemgetter
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
from networkx.algorithms import community

#read the csv table of relationships we want to graph
raw_data = pd.read_csv('linked nodes.csv')

#print to view data
print(raw_data)

#unpivot the data so that we have our data into a two column edge list. 
melted_data = raw_data.melt(['Account'],value_vars =['US','CANADA','MEXICO'],var_name = 'Relationship')
## need to figure out how to store country column header as an attribute variable for the edge list
## right now relation ship arrows are dicted by the value given in the account column
##
## Example:
## in our list we have (Account(1),'Any Country Column'(2))
## we draw this relationship as (1) --- > (2)

## jf later in the list we see (Account(2),'Any Country Column'(1))
## we draw update the two nodes to look like this  (1) < --- > (2)
## 
## We cannot show  a relationship between a unique entry value and its column value

#creates a graph made of the edgelist we formatted above
G = nx.from_pandas_edgelist(melted_data, source = "Account", edge_attr = True, target = "value", create_using=nx.DiGraph)


#Allow the user to choose what kind of network matrix they would like to create
userGraph = input("Choose a network matrix to draw: (C)ircular, (N)etwork: ")
if userGraph == "Circular" or "C":
    nx.draw_circular(G,with_labels = True)


elif userGraph == "Network" or  "N":
    nx.draw_networkx(G,with_labels = True)
else:
    nx.draw(G,with_labels = True)

#draws and displays graph using matplotlab
plt.draw()
plt.show()


###TO DO####

##Key nodes with their respective country then group nodes by their country

##verify network accuracy