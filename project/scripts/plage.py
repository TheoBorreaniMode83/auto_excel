class Plage:
    
    def __subGestionErreurConstructeur(self,arg,name,isGood):
        if(type(arg)==None):
            isGood=False
            print(f"Pour créer une plage l'argument {name} est obligatoire")
        elif(type(arg)!=int):
            isGood=False
            print(f"Pour créer une plage l'argument {name} doit etre un entier")
        elif(arg<=0):
            isGood=False
            print(f"Pour créer une plage l'argument {name} doit etre strictement positif")
        return isGood
    
    def __subGestionErreurConstructeur2(self,arg1,arg2,name1,name2,isGood):
        if(arg1>arg2):
            isGood=False
            print(f"Pour créer une plage l'argument {name2} doit etre supérieur ou égal à l'argument {name1} ")
        return isGood

    def __gestionErreurConstructeur(self,minRow,maxRow,minColumn,maxColumn):
        isGood=True

        isGood = self.__subGestionErreurConstructeur(minRow,"minRow",isGood)
        isGood = self.__subGestionErreurConstructeur(maxRow,"maxRow",isGood)
        isGood = self.__subGestionErreurConstructeur(minColumn,"minColumn",isGood)
        isGood = self.__subGestionErreurConstructeur(maxColumn,"maxColumn",isGood)
        isGood = self.__subGestionErreurConstructeur2(minRow,maxRow,"minRow","maxRow",isGood)
        isGood = self.__subGestionErreurConstructeur2(minColumn,maxColumn,"minColumn","maxColumn",isGood)
        if(isGood==False):
            raise Exception("Plage fausse")
      
    def __init__(self, minRow=None, maxRow=None, minColumn=None, maxColumn=None):
        self.__gestionErreurConstructeur(minRow,maxRow,minColumn,maxColumn)
        self.minRow=minRow
        self.maxRow=maxRow
        self.minColumn=minColumn
        self.maxColumn=maxColumn