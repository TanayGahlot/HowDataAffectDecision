#oggpnosn
#hkhr

#extracting friends facebook data

from pymongo import Connection 
import facebook

#using acces token to access facebook api
graph=facebook.GraphAPI("CAACEdEose0cBAAHnRU7OESSY840ztx7DcqfEoS9vlQPCRZAyLdPo0faQMkCDrOZB7oDSe3vcckZAOFBvAclV74LbyF3miaLXSIwvO8ZCfZCWT2ckkdv2uLcfkrI65HI6smerifZAtVK0CA4mIT5vbSbAvv5ZCKgC7yuggsN3SkrA8aXWmB9Y5YcXfvyRcIslCbh9XRH2pt3ZCgZDZD")
friends=graph.get_object("/me/friends")
friends=friends['data']

c=Connection()
dbh=c['FAmey']

for friend in friends:
    dbh.friend.insert(graph.get_object("/"+friend['id']),safe=True)
    print "Inserted Data of "+friend['name']


