from SPRJUDToSQL import *




"""
création des tables de test:
c.execute('''CREATE TABLE CITY(Name text, Country text, Population real)''')
c.execute('''CREATE TABLE COUNTRY(Name text, Capital text, Population real, Currency text)''')

c.execute("INSERT INTO CITY VALUES ('Bergen','Belgium',20.3)")
c.execute("INSERT INTO CITY VALUES ('Bergen','Norway',30.5)")
c.execute("INSERT INTO CITY VALUES ('Brussels','Belgium',370.6)")
c.execute("INSERT INTO COUNTRY VALUES ('Belgium','Brussels',10225.6,'EUR')")
"""
try:
   traducteur = SPRJUDToSQL()
   traducteur.selectDataBase('test.db')

   traducteur.traductionAndExecution(Select(Eq(Attribut('Name'), Cst('Bergen')), Relation('CITY', ['test3'])))

   traducteur.traduction(Union(Relation('CITY',['test1']), Relation('COUNTRY',['test2'])))
   traducteur.traduction(Difference(Relation('CITY',['test1']), Relation('COUNTRY',['test2'])))
   traducteur.traduction(Difference(Select(Eq(Attribut('Name'), Cst('Bergen')), Relation('CITY', ['test3'])), Relation('COUNTRY',['test2'])))
   traducteur.traduction(Union(Select(Eq(Attribut('a'), Cst('b')), Relation('NomRelation', ['test3'])), Relation('COUNTRY',['test2'])))
except TypeError as inst:
         print(inst.args)
