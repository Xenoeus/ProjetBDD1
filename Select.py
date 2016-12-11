from Expression import Expression
from Eq import Eq
from Relation import Relation

class Select(Expression):
   """
   Cette classe represente la selection en SPJRUD.
   """

   def __init__(self, egalite, relation):
      self.egalite = egalite
      self.relation = relation
      self.query = "SELECT * FROM "+str(self.relation)+" WHERE "+str(self.egalite)

   def __str__(self):
      return self.query