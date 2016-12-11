from Expression import Expression
from Attribut import Attribut
from Relation import Relation

class Project(Expression):

   """
   Cette classe represente la projection en SPJRUD.
   """
   def __init__(self, attributs, relation): 
      self.attributs = attributs
      self.relation = relation
      self.query = "SELECT "+str(self.attributs)+" FROM "+str(self.relation)

   def __str__(self):
      return self.query