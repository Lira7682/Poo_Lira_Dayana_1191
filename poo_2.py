print(" ")
print("Lira Hernandez Dayana Yamileth 1191")
print(" ")

class Persona():
    def __init__(self , nombre , edad):
        self.nombre = nombre
        self.edad = edad
    def cumpleaños(self): 
        self.edad += 1
p = Persona("Briana", 25)  
p.cumpleaños() 
print(f"{p.nombre} cumple {p.edad} años")
print(" ")