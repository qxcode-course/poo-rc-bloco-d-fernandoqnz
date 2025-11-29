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
    def __init__(self,name:str):
        self.__name= name
        self.__phones: list[Phone] = []
        self.__favorited=False

    def getName(self):
        return self.__name
    
    def getIsfavorited(self):
        return self.__favorited
    
    def getPhones(self):
        return self.__phones
    
    def favorite(self):
        self.__favorited=True

    def unfavorited(self):
        self.__favorited=False

    def  addPhone(self, phone:Phone):
        if phone.isValid(phone.getNumber()):
            self.__phones.append(phone)
            return True
        print("fail: invalid number")
        return False
        

    def rmPhone(self, index:int):
        if 0 <= index <len(self.__phones):
            del self.__phones[index]
            return True
        print("fail: telefone inexistente")
        return False 

    def __str__(self):
        fav = "@" if self.__favorited else "-"

        if len(self.__phones) == 0:
            phones_str="[]"
            return f"{fav} {self.__name} {phones_str}"
        
        phones_inside = ", ".join(f"{p.getId()}:{p.getNumber()}" for p in self.__phones)
        return f"{fav} {self.__name} [{phones_inside}]"
    
def main():
    contact =Contact("")
    while True:
        line=input()
        args=line.split(" ")
        print(f"${' '.join(args)}")
        cmd = args[0]

        if cmd == "show": 
            print(contact)

        elif cmd=="end":
            break

        elif cmd =="init":
            contact = Contact(args[1])

        elif cmd == "add":
            id= args[1]
            number= args [2]
            contact.addPhone(Phone(id, number))

        elif cmd == "rm":
            index = int(args[1])
            contact.rmPhone(index)

        elif cmd == "tfav":
            if contact.getIsfavorited():
                contact.unfavorited()
            else:
                contact.favorite()

        else: 
            print("comando invdo")

main()





        

    

        

