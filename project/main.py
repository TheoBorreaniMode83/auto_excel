#!/usr/bin/python

from scripts import header
from scripts import matrice_intermediaire
from scripts import plage
from scripts import gst_base_donnees_sql_lite
from openpyxl import load_workbook
import csv
import os

#STEP0 Def des fonctions utilisé dans functionOnColumn 
#qui ont comme signature entrée : string, sortie: string
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
    
#STEP1 réglages des variables
pathFichier="fichiers_entree/Classeur1.xlsx"
nomFeuille="Feuil1"
minRow = 2
maxRow = 20
minColumn = 1
maxColumn = 5
headert=header.Header([("ID","int"),("Prenom","string"),("Portefeuille",'double'),("Numero","int"),("Date_de_naissance","string")])

#STEP2 création et modification de la matrice
matrice = matrice_intermediaire.MatriceIntermaidiaire(pathFichier, nomFeuille, plage.Plage(minRow,maxRow,minColumn,maxColumn),headert)
matrice.afficheMatrice(" | ")
matrice.functionOnColumn(3,delSpace)
print()
matrice.afficheMatrice(" | ")
matrice.echangeRow(1,4)
print()
matrice.afficheMatrice(" | ")
matrice.insertRow(["20","2000-08-30 00:00:00","54","0649858572","Theo"],0)
print()
matrice.afficheMatrice(" | ")
matrice.functionOnColumn(1,lambda a : "a")
print()
matrice.afficheMatrice(" | ")
matrice.deleteRow(1)
print()
matrice.afficheMatrice(" | ")
#STEP3 interaction avec la base de données
db = gst_base_donnees_sql_lite.GstBaseDonnees("fichiers_sortie/baseDonnees.db")
db.executeRequete("""
    CREATE TABLE IF NOT EXISTS maTable (
        ID int(5) NOT NULL,
        Prenom varchar(50) DEFAULT NULL,
        Portefeuille DOUBLE DEFAULT NULL,
        Numero INT,
        Date_de_naissance varchar(50) ,
        PRIMARY KEY(ID)
    );
    """)
db.writeMatrice("maTable",matrice)
db.executeRequete("""SELECT * FROM maTable""")
print()
print(db.cursor.fetchone())
