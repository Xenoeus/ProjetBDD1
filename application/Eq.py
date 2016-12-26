from Expression import Expression
from Attribut import Attribut
from Cst import Cst

class Eq(Expression):
   """
   Cette classe represente une egalite. Elle est surtout utilisee avec la classe ``Select``
   pour dire qu'un attribut egale une constante ou un autre attribut.
   """

   def __init__(self, attribut1, attribut2, signe):
      self.attribut1 = attribut1
      self.attribut2 = attribut2
      self.signe = signe
      self.nomExpression = "Eq("+ attribut1.nomExpression+","+ attribut2.nomExpression+")"

   def __str__(self):
      return str(self.attribut1)+" "+self.signe+" "+str(self.attribut2)
