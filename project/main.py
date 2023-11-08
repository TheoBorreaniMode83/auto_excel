#!/usr/bin/python

from scripts import header
from scripts import matrice_intermediaire
from scripts import plage
from scripts import gst_base_donnees_sql_lite
from openpyxl import load_workbook
import csv
import os

i=-1
##STEP_1 Def des fonctions utilisé dans functionOnColumn qui ont comme signature entrée : string, sortie: string
def majuscule(string):
    return string.upper()
def minuscule(string):
    return string.lower()
def virgulesDeviennentPoints(string):
    return string.replace(',','.')
def delSpace(string):
    try:
        return string.replace(' ','')
    except: 
        return ""
def autoIncrement(string):
    global i 
    i=i+1
    return str(i)
##STEP_2 réglages des variables
pathFichier="fichiers_entree/Classeur1.xlsx"
nomFeuille="Feuil1"
#minRow, maxRow, minColumn, maxColumn permette de selectionner une plage de cellule dans le fichier excel 
minRow = 2        
maxRow = 20
minColumn = 1
maxColumn = 5
#header contient le titre et le type de valeur de notre futur matrice
header=header.Header([("ID","int"),("Prenom","string"),("Portefeuille",'double'),("Numero","int"),("Date_de_naissance","string")])

##STEP_3 création et modification de la matrice
matrice = matrice_intermediaire.MatriceIntermaidiaire(pathFichier, nomFeuille, plage.Plage(minRow,maxRow,minColumn,maxColumn),header)
matrice.functionOnColumn(3,delSpace)
matrice.echangeColumn(1,4)
matrice.insertRow(["20","2000-08-30 00:00:00","54","0649858572","Theo"],0)
matrice.functionOnColumn(1,lambda a : "a")
matrice.afficheMatrice(" | ")
matrice.insertColumn(1, "Age", "int")
matrice.functionOnColumn(0,autoIncrement)
matrice.afficheMatrice(" | ")
matrice.deleteColumn(1)



##STEP_4 
print(matrice.getSqlInsert("Nom_de_ma_table"))

#db = gst_base_donnees_sql_lite.GstBaseDonnees("fichiers_sortie/baseDonnees.db")
#db.executeRequete("""
#    CREATE TABLE IF NOT EXISTS maTable (
#        ID int(5) NOT NULL,
#        Prenom varchar(50) DEFAULT NULL,
#        Portefeuille DOUBLE DEFAULT NULL,
#        Numero INT,
#        Date_de_naissance varchar(50) ,
#        PRIMARY KEY(ID)
#    );
#    """)
#db.writeMatrice("maTable",matrice)
#db.executeRequete("""SELECT * FROM maTable""")
#print()
#print(db.cursor.fetchone())
