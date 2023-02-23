#Carbajal Martinez
#Hernández Hernández 
#Roque Hernández

class reparaciones:
    def __init__(self, mantenimiento, joystiks, reballing, flex, costo):
        self.mantenimiento = mantenimiento
        self.joysticks = joystiks
        self.reballing = reballing
        self.flex = flex
        self.__costo = costo

tipo = input('Que servicio deseas cotizar?: ')

if tipo == "mantenimiento":
    cuantos = int(input('A cuantos equipos se le dará el servicio?: '))
    costo = cuantos*650
    print(f'El costo total sería {costo}')

if tipo == "joysticks":
    cuantos = int(input('A cuantos equipos se les reparará el joystick?: '))
    costo = cuantos*250
    print(f'El costo total sería {costo}')

if tipo == "reballing":
    cuantos = int(input('A cuántos equipos se les dará reballing?: '))
    costo = cuantos*1200
    print(f'El costo total sería {costo}')

if tipo == "flex":
    Tflex = input('Será flex de celular o laptop?: ')
    if Tflex == "celular":
        cuantos = int(input('A cuántos se les cambiará el flex?: '))
        costo = cuantos*750
        print(f'El costo total sería {costo}')
    else:
        cuantos = int(input('A cuántas laptops se les cambiará el flex?: '))
        costo = cuantos*1400
        print(f'El costo total sería {costo}')