from Relation import Relation
from Expression import Expression
from Attribut import Attribut
from Cst import Cst

class Rename(Expression):
   """
   Cette classe represente le renommage en SPJRUD
   """
    
   def __init__(self, nom_initial, nouveau_nom, relation):
      self.nom_initial = nom_initial
      self.nouveau_nom = nouveau_nom
      self.relation = relation
      self.query = "SELECT "+str(self.nom_initial)+" AS "+str(self.nouveau_nom)+" FROM "+str(self.relation)

   def __str__(self):
      return self.query