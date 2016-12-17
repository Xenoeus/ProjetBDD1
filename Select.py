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
      self.verifieAttributs()
      self.query = "SELECT * FROM "+str(self.relation)+" WHERE "+str(self.egalite)
      self.colonnes = relation.colonnes

   def __str__(self):
      return self.query

   def verifieAttributs(self):
      """
      Cette methode verifie si les valeurs entrees dans le constructeur
      sont bien celles que l'on attend.
      """
      if not isinstance(self.egalite, Eq):
         raise TypeError("L'attribut egalite doit etre un objet de type Eq")
      elif not isinstance(self.relation, Relation) and not isinstance(self.relation, Expression):
         raise TypeError("L'attribut relation doit etre un objet de type Relation ou Expression")
