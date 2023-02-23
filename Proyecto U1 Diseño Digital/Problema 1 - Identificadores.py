#Carbajal Martinez
#Hernández Hernández 
#Roque Hernández

class Persona:
    def __init__(self, nombre, edad, DNI):
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI

    def mostrar(self):
            print(f'El nombre es {self.nombre}, tiene {self.edad} años y su DNI es {self.DNI}')

    def esMayordeEdad(self):
        if self.edad > 18:
            return True
        else:
            return False
        
datos=Persona("Jenni",19,21560304)
datos.mostrar()
print(f'¿Es mayor de edad?')
print(datos.esMayordeEdad())