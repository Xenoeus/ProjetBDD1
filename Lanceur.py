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
import sqlite3
connection = sqlite3.connect('test.db')

c = connection.cursor()



"""
création des tables de test:
c.execute('''CREATE TABLE CITY(Name text, Country text, Population real)''')
c.execute('''CREATE TABLE COUNTRY(Name text, Capital text, Population real, Currency text)''')

c.execute("INSERT INTO CITY VALUES ('Bergen','Belgium',20.3)")
c.execute("INSERT INTO CITY VALUES ('Bergen','Norway',30.5)")
c.execute("INSERT INTO CITY VALUES ('Brussels','Belgium',370.6)")
c.execute("INSERT INTO COUNTRY VALUES ('Belgium','Brussels',10225.6,'EUR')")
"""
connection.commit()

stri = Select(Eq(Attribut('Name'), Cst('Bergen')), Relation('CITY', ['test3'])).string_query()
print(stri)
c.execute(stri)

print(c.fetchall())
try:
   Union(Relation('CITY',['test1']), Relation('COUNTRY',['test2'])).print_query()
   #Union('bou', 1).print_query()
except TypeError as inst:
    print(inst.args)
try:
   Difference(Relation('CITY',['test1']), Relation('COUNTRY',['test2'])).print_query()
except TypeError as inst:
    print(inst.args)
try:
   Difference(Select(Eq(Attribut('Name'), Cst('Bergen')), Relation('CITY', ['test3'])), Relation('COUNTRY',['test2'])).print_query()
except TypeError as inst:
    print(inst.args)
try:
   Union(Select(Eq(Attribut('a'), Cst('b')), Relation('NomRelation', ['test3'])), Relation('COUNTRY',['test2'])).print_query()
except TypeError as inst:
   print(inst.args)

connection.rollback()
connection.close()
