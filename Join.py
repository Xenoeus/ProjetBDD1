from Relation import Relation
from Expression import Expression

class Join(Expression):
    
    def __init__(self, relation1, relation2):
    	self.relation1 = relation1
    	self.relation2 = relation2
    	self.query = "SELECT * FROM "+str(relation1)+" NATURAL JOIN "+str(relation2)
