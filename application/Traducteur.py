from Expression import *
from Relation import *
from Select import *
from Project import *
from Join import *
from Rename import *
from Union import *
from Difference import *
from Attribut import *
from Cst import *



class Traducteur():


   def traduction(self, SPRJUD):
      """
      Cette methode permet de traduire une requête de sprjud en sql elle revoit true si l'opération c'est bien passée et false sinon
      """
      SPRJUD.autorisation()
      return SPRJUD


