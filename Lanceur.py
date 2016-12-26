from SPRJUDToSQL import *



connection = sqlite3.connect('test2.db')
c = connection.cursor()
a = '''CREATE TABLE CITY(Name text, Country text, Population real)'''
c.execute(a)
c.execute('''CREATE TABLE COUNTRY(Name text, Capital text, Population real, Currency text)''')
c.execute('''CREATE TABLE TEST(Mon Numeric, Capital text, Population real, Currency text)''')

c.execute("INSERT INTO CITY VALUES ('Bergen','Belgium',20.3)")
c.execute("INSERT INTO CITY VALUES ('Bergen','Norway',30.5)")
c.execute("INSERT INTO CITY VALUES ('Brussels','Belgium',370.6)")
c.execute("INSERT INTO COUNTRY VALUES ('Belgium','Brussels',10225.6,'EUR')")
c.execute("INSERT INTO TEST VALUES ('10','Brussels',10225.6,'EUR')")
connection.commit()
connection.close()


traducteur = SPRJUDToSQL()
traducteur.selectionDataBase('test2.db')


test = Select(Eq(Attribut('Name'), Cst('Bergen'), "="), Relation('CITY'))
traducteur.traductionEtExecution(test)

traducteur.traduction(Union(Relation('CITY'), Relation('COUNTRY')))

traducteur.traduction(Difference(Relation('CITY'), Relation('COUNTRY')))
traducteur.traduction(Difference(Select(Eq(Attribut('Name'), Cst('Bergen'),"="), Relation('CITY')), Relation('COUNTRY')))
traducteur.traduction(Union(Select(Eq(Attribut('a'), Cst('b'),">"), Relation('NomRelation')), Relation('COUNTRY')))

traducteur.traduction(Union(Relation('MAMAN'), Relation('COUNTRY')))

g = Attribut('Name')
h = Attribut('Country')
n = [g,h]
traducteur.traduction(Project(n,Relation('CITY')))

g = Attribut('MON')
h = Attribut('Country')
n = [g,h]
traducteur.traduction(Project(n,Relation('CITY')))

traducteur.traductionEtExecution(Union(Relation('TEST'), Relation('COUNTRY')))

traducteur.traductionEtCreationDeTable(test , "Bob")
