class Mago:
    def hechizos(self):
        print("Dice: permiso que voy a hace un hechizo")

class Guerrero:
    def defensa(self):
        print("Se está defendiendo wazaaa")

class Elfo:
    def aura(self):
        print("Está aumentando su aura (elfo rizz)")

class DarkLord(Guerrero, Elfo):
    pass

dark_lord = DarkLord()  
dark_lord.defensa()   
dark_lord.aura()     
print(DarkLord.__mro__)  

class DarkLord(Elfo,Guerrero):
    pass

dark_lord = DarkLord()
dark_lord.aura() 
dark_lord.defensa()        
print(DarkLord.__mro__)  
