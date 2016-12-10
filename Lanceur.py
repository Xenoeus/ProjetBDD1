from Expression import *
from Eq import *
from Relation import *
from Select import *
from Project import *
from Join import *
from Rename import *
from Union import *
from Difference import *
from Attribut import *
from Cst import *

Union(Relation('CITY',['test1']), Relation('COUNTRY',['test2'])).print_query()
Select(Eq(Attribut('a'), Cst('b')), Relation('NomRelation', ['test3'])).print_query()

Union(Select(Eq(Attribut('a'), Cst('b')), Relation('NomRelation', ['test3'])), Relation('COUNTRY',['test2'])).print_query()