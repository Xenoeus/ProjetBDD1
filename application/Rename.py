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
      self.colonnes = relation.colonnes
      self.nomExpression = "Rename("+ nom_initial+","+nouveau_nom+","+relation.nomExpression+")"


   def autorisation(self):
      """
      Cette methode verifie que toutes les conditions sont respectee, après cela elle traduis l'expression.
      """
      if isinstance(self.relation, Expression):
         self.relation.autorisation()
      if isinstance(self.relation1, Relation):
         if (self.relation.verifieTable()):
            raise TypeError("Ce nom de relation n'est pas correct ou cette relation n'existe pas :\"" + self.relation.nom + "\"")
      self.verifieAttributs()
      self.query = "SELECT "+str(self.nom_initial)+" AS "+str(self.nouveau_nom)+" FROM "+str(self.relation)
      self.rename()

   def __str__(self):
      return self.query

   def verifieAttributs(self):
      """
      Cette methode verifie si les valeurs entrees dans le constructeur
      sont bien celles que l'on attend.
      """
      if not isinstance(self.relation, Relation) and not isinstance(self.relation, Expression):
         raise TypeError("L'attribut relation doit etre un objet de type Relation ou Expression")
      elif not isinstance(self.nom_initial, Attribut):
         raise TypeError("L'attribut nom_initial doit etre un objet de type Attribut")
      elif not isinstance(self.nouveau_nom, Cst):
         raise TypeError("L'attribut nouveau_nom doit etre un objet de type Cst")

   def rename(self):
      """
      Renomme la colonne qui doit etre renommee
      """
      for i in self.colonnes:
         if (i == self.nouveau_nom):
            self.colonnes[i][0] = self.nouveau_nom
