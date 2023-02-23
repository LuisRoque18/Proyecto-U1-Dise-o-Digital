#Carbajal Martinez
#Hernández Hernández 
#Roque Hernández

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_edad(self, edad):
        self.edad = edad

    def get_nombre(self):
        return self.nombre
    
    def get_edad(self):
        return self.edad
    
    def mostrar_persona(self):
        print(f'Su nombre es {self.nombre} y su edad es {self.edad} años')

    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return "Si" 
        else:
            return "No"
        
    def es_mayor_que(self, otro):
        if self.edad > otro.get_edad():
            return "Si"
        else:
            return "No"
        
persona1 = Persona("Lorenzo", 17)
persona2 = Persona("Andres", 20)

persona1.mostrar_persona()
persona2.mostrar_persona()

print(f'\n¿{persona1.get_nombre()} es mayor que {persona2.get_nombre()}? {persona1.es_mayor_de_edad()}')
print(f'¿{persona2.get_nombre()} es mayor que {persona1.get_nombre()}? {persona2.es_mayor_de_edad()}')

print(f'\n{persona1.get_edad()} es mayor que {persona2.get_edad()}? {persona1.es_mayor_que(persona2)}')
print(f'{persona2.get_edad()} es mayor que {persona1.get_edad()}? {persona2.es_mayor_que(persona1)}')