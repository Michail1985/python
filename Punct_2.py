class Road:

    def __init__(self, length, width):
        _self_lenght = length
        _self_width = width
        _mass = [25, 5]
        mass_asphalt = _self_lenght*_self_width*_mass[0]*_mass[1]/1000
        print(mass_asphalt)

r = Road(5000, 20)