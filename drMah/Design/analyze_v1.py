#oggpnosn
#hkhr

#importing essential
from pymongo import Connection

#establishing a connection
c=Connection(host="localhost",port=27017)

#creating a database handle
try:
    dbh=c["drMah"]
except:
    print "Could not connect to database"


#function to search for free volunteer
def freeVolunteer():
    
