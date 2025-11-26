class Phone:
    def __init__(self, id:str, number:str) :
        self.__id = id
        self.__number = number


    def isValid (self, number:str):
        permitidos = "0123456789()."
        for c in number:
            if c not in permitidos:
                return False
        return True
    
    def getNumber(self):
        return self.__number 
    
    def getId(self):
        return self.__id

    def __str__(self):
        return f"{self.__id}:{self.__number}"

class Contact:
    def __init__(self, name=""):
        if name is None: name = ""
        self.__name = name
        self.__fones = []
        self.__favorited = False
    
    def addPhone(self, label, number):
        fone = Phone(label, number)
        if not fone.isValid(number):
          print("fail: fone invalido")
            return False
        self.__fones.append(fone)
        return True

        


        

        

