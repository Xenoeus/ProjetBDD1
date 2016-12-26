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
      attr = []
      for i in attributs:
         attr.append(i.nomExpression)
      self.nomExpression = "Project("+str(attr)+","+relation.nomExpression+")"

   def autorisation(self):
      """
      Cette methode verifie que toutes les conditions sont respectee, après cela elle traduis l'expression.
      """
      if isinstance(self.relation, Expression):
         self.relation.autorisation()
      if isinstance(self.relation, Relation):
         if (self.relation.verifieTable()):
            raise TypeError("Ce nom de relation n'est pas correct ou cette relation n'existe pas :\"" + self.relation.nom + "\"")
      self.verifieAttributs()
      self.colonnes = self.selectionColonnes()
      self.compiler()
      self.query = "SELECT "+self.affichageListe+" FROM "+str(self.relation)

   def __str__(self):
      return self.query

   def verifieAttributs(self):
      """
      Cette methode verifie si les valeurs entrees dans le constructeur
      sont bien celles que l'on attend.
      """
      if not isinstance(self.attributs, list) or len(self.attributs) == 0:
         raise TypeError("Le premier attribut de Project doit etre une liste non vide d'objets Attribut")
      elif not isinstance(self.relation, Relation) and not isinstance(self.relation, Expression):
         raise TypeError("Le second attribut de Project doit etre un objet de type Relation ou Expression")
      for e in self.attributs:
         if not isinstance(e, Attribut):
            raise TypeError("Les elements de la liste du premier attribut de Project doivent etre de type Attribut")
      for g in self.attributs:
         if not (self.verifieColonnes(g)):
            raise TypeError(g.nom + " n'est pas un nom de colonnes existant dans la relation/l'expression:" + self.relation.nom)

   def compiler(self):
      """
      Cette methode permet l'affichage des elements de la liste d'attributs
      """
      self.affichageListe = ""
      for i in self.attributs:
         self.affichageListe = self.affichageListe + str(i) + ","
      self.affichageListe = self.affichageListe[:len(self.affichageListe)-1]

   def verifieColonnes(self, nom):
      """
      Cette methode verifie qu'une colonne existe dans la relation/ l'expression donnee. Elle retourne True si elle existe false sinon
      """
      for i in self.relation.colonnes:
         if(nom.nom == i[0]):
            return True
      return False

   def selectionColonnes(self):
      """
      Cette methode permet de selectionner les colonnes demandee par attributs
      """
      colonnes = []
      for nom in self.attributs:
         for i in self.relation.colonnes:
            if(nom.nom == i):
               colonnes.append(i)
      return colonnes
            
