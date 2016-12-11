from Relation import Relation
from Expression import Expression

class Union(Expression):
   """
   Cette classe represente l'union en SPJRUD
   """
    
   def __init__(self, relation1, relation2):
      self.relation1 = relation1
      self.relation2 = relation2
      self.query = "SELECT * FROM "+str(self.relation1)+" UNION SELECT * FROM "+str(self.relation2)

   def __str__(self):
      return self.query



