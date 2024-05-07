class Produccion:
    def produccion(self, cultivos, animales):
        produccion_cultivos = sum(cultivo.rendimiento for cultivo in cultivos)
        produccion_animales = sum(animal.peso for animal in animales)
        return produccion_cultivos, produccion_animales


class Cultivo:
    def __init__(self, nombre, tipo, area_cultivo, rendimiento):
        self.nombre = nombre
        self.tipo = tipo
        self.area_cultivo = area_cultivo
        self.rendimiento = rendimiento


class Animal:
    def __init__(self, especie, raza, edad, peso):
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.peso = peso


class Granja:
    def __init__(self):
        self.cultivos = []
        self.animales = []

    def agregar_cultivo(self, cultivo):
        self.cultivos.append(cultivo)

    def eliminar_cultivo(self, cultivo):
        self.cultivos.remove(cultivo)

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def eliminar_animal(self, animal):
        self.animales.remove(animal)

    def produccion_total(self):
        calculadora = Produccion()
        produccion_cultivos, produccion_animales = calculadora.produccion(self.cultivos, self.animales)
        return produccion_cultivos, produccion_animales



if __name__ == "__main__":
    
    cultivo1 = Cultivo("Maíz", "Cereal", 100, 500)  
    cultivo2 = Cultivo("Trigo", "Cereal", 150, 600)
    cultivo3 = Cultivo("Papa", "Tuberculo", 300, 900)
    
    animal1 = Animal("Vaca", "Angus", 5, 400)  
    animal2 = Animal("Gallina", "Leghorn", 2, 2)
    animal3 = Animal("Cerdo", "Iberico", 6, 300)
    
    
    granja_ucundinamarca = Granja()
    
    
    granja_ucundinamarca.agregar_cultivo(cultivo1)
    granja_ucundinamarca.agregar_cultivo(cultivo2)
    granja_ucundinamarca.agregar_cultivo(cultivo3)
    granja_ucundinamarca.agregar_animal(animal1)
    granja_ucundinamarca.agregar_animal(animal2)
    granja_ucundinamarca.agregar_animal(animal3)
    
    
    produccion_cultivos, produccion_animales = granja_ucundinamarca.produccion_total()
    print("Produccion total de los cultivos es:", produccion_cultivos)
    print("Produccion total de los animales es:", produccion_animales)
    print("La produccion total de la granja es:", produccion_cultivos+produccion_animales)