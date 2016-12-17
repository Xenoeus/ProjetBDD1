from Relation import Relation
from Expression import Expression

class Difference(Expression):
   """
   Cette classe represente la difference en SPJRUD
   """
    
   def __init__(self, relation1, relation2):
      self.relation1 = relation1
      self.relation2 = relation2
      self.verifieAttributs(relation1, relation2)
      self.query = "SELECT * FROM "+str(self.relation1)+" MINUS SELECT * FROM "+str(self.relation2)
      self.colonnes = relation1.colonnes

   def __str__(self):
      return self.query

   def verifieAttributs(self, relation1, relation2):
      """
      Cette methode verifie si les valeurs entrees dans le constructeur
      sont bien celles que l'on attend.
      """
      if not isinstance(self.relation1, Relation) and not isinstance(self.relation1, Expression):
         raise TypeError("L'attribut relation1 doit etre un objet de type Relation ou Expression")
      elif not isinstance(self.relation2, Relation) and not isinstance(self.relation2, Expression):
         raise TypeError("L'attribut relation2 doit etre un objet de type Relation ou Expression")
      if(len(relation1.colonnes) != len(relation2.colonnes)):
         raise TypeError("Les deux expression(s)/relation(s) de : Difference(" + str(self.relation1) + "," + str(self.relation2) + ") , doivent avoir le même nombre de colonnes")
