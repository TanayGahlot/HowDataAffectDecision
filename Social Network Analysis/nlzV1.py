#oggpnosn
#hkhr

#importing pymongo and networkx for database and network analysis

from pymongo import Connection
import networkx as nx

#establishing connection with database
print "Establishing Connection"
C=Connection()

#initializing Graph Object
print "Initializing Graph"
g=nx.Graph()

#collectiog Tanay Gahlots Data 
print "Extracing Tanay's Data"
dbh=C["Facebook_Friends"]
friends=dbh.friend.find()
for friend in friends:
    g.add_edge("Tanay Gahlot",friend["name"])

#collecting Anuja's Data
print "Extracing Anuja's Data"
dbh=C["FAnuja"]
friends=dbh.friend.find()
for friend in friends:
    g.add_edge("Anuja Deshpande",friend["name"])


#collecting Amey's Data
print "Extracing Amey's Data"
dbh=C["FAmey"]
friends=dbh.friend.find()
for friend in friends:
    g.add_edge("Amey Kamat",friend["name"])

nx.write_gexf(g,"ata.gexf")
