from Relation import Relation
from Expression import Expression

class Rename(Expression):
    
    def __init__(self, nom_initial, nouveau_nom, relation):
    	self.nom_initial = nom_initial
    	self.nouveau_nom = nouveau_nom
    	self.relation = relation
    	self.query = 