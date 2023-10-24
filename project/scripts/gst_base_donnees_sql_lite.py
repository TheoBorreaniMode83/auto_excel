# coding: utf-8

from scripts import matrice_intermediaire


import sqlite3

class GstBaseDonnees:
    def __init__(self, cheminBDD):
        self.conn = sqlite3.connect(cheminBDD)
        self.cursor = self.conn.cursor()

    def executeRequete(self,requete):
        self.cursor.execute(requete)

    def writeMatrice(self,table, matrice):
        string1 = ""
        string2 = ""
        for i in range(len(matrice.header.header)):
            string1=string1+matrice.header.header[i][0]
            if(i<len(matrice.header.header)-1):
                string1=string1+", "

        for i in range(len(matrice.content)):
            for ii in range(len(matrice.content[0])):
                if(ii==0):
                    string2=string2+"("
                if(matrice.header.header[ii][1]=="string"):
                    string2=string2+"'"+matrice.content[i][ii]+"'"
                else:
                    string2=string2+matrice.content[i][ii]

                if(ii<len(matrice.content[0])-1):
                    string2=string2+", "
                elif(i<len(matrice.content)-1):
                    string2=string2+"),"
                else:
                    string2=string2+")"
        self.cursor.execute(f"""INSERT INTO {table} ({string1}) VALUES {string2};""")# a remplacer part cursor.execute
        print(f"""INSERT INTO {table} ({string1}) VALUES {string2};""")# a remplacer part cursor.execute
