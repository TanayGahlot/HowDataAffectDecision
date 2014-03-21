#oggpnosn
#hkhr

#simulating the actual 

#defining a position in 2d space
class Location(object):
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def getX(self):
		return self.x
	def getY(self):
		return self.y
	def distance(other):
		return ((self.x-other.x)**2+(self.y-other.y)**2)**.5
		

#defining a person 
class Person(object):
	def __init__(self,name,location):
		self.name=name
		self.location=location
	def getName(self):
		return self.name
	def getLocation(self):
		return self.location

#defining the volunteer
class Volunteer(Person):
	def __init__(self,name,location):	
		Person.__init__(self,name,location)
		self.status=True
	def isFree(self):
		return self.status
	

