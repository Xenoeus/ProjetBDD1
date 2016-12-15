from Relation import Relation
from Expression import Expression

class Difference(Expression):
   """
   Cette classe represente la difference en SPJRUD
   """
    
   def __init__(self, relation1, relation2):
      self.relation1 = relation1
      self.relation2 = relation2
      self.verifieAttributs()
      self.query = "SELECT * FROM "+str(self.relation1)+" MINUS SELECT * FROM "+str(self.relation2)

   def __str__(self):
      return self.query

   def verifieAttributs(self):
      """
      Cette methode verifie si les valeurs entrees dans le constructeur
      sont bien celles que l'on attend.
      """
      if not isinstance(self.relation1, Relation) and not isinstance(self.relation1, Expression):
         raise TypeError("L'attribut relation1 doit etre un objet de type Relation ou Expression")
      elif not isinstance(self.relation2, Relation) and not isinstance(self.relation2, Expression):
         raise TypeError("L'attribut relation2 doit etre un objet de type Relation ou Expression")
