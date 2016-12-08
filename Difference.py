from Relation import Relation
from Expression import Expression

class Difference(Expression):
    
    def __init__(self, relation1, relation2):
    	self.relation1 = relation1
    	self.relation2 = relation2
    	self.query = "SELECT * FROM "+str(self.relation1)+" MINUS SELECT * FROM "+str(self.relation2)
