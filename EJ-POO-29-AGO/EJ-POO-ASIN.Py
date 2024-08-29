# Encapsulamiento: en toda la clase veiculo se crean los atributos que despues
# van a poder heredar auto, moto y camion.
class Vehiculo():
    def __init__(self, marca, modelo, año):
        self.__marca = marca 
        self.__modelo = modelo
        self.__año = año
        
    def get_marca(self): 
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_año(self):
        return self.__año

    def set_año(self, año):
        self.__año = año

    def acelerar(self):
        pass
    
    def detener(self): 
        pass

# Herencia: como mencione arriba la clase auto hereda a vehiculo lo mismo sucede con moto y camion
class Auto(Vehiculo):  
    def __init__(self, marca, modelo, año, puertas):
        super().__init__(marca, modelo, año)
        self.__puertas = puertas

    def get_puertas(self):
        return self.__puertas

    def set_puertas(self, puertas):
        self.__puertas = puertas

    def acelerar(self): 
        print(f"El auto {self.get_marca()} {self.get_modelo()} está acelerando.")
    
    def detener(self): 
        print(f"El auto {self.get_marca()} {self.get_modelo()} se ha detenido.")

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, cilindrada):
        super().__init__(marca, modelo, año)
        self.__cilindrada = cilindrada

    def get_cilindrada(self):
        return self.__cilindrada

    def set_cilindrada(self, cilindrada):
        self.__cilindrada = cilindrada

    def acelerar(self):
        print(f"La motocicleta {self.get_marca()} {self.get_modelo()} con cilindrada de {self.get_cilindrada()}cc está acelerando.")
    
    def detener(self):
        print(f"La motocicleta {self.get_marca()} {self.get_modelo()} se ha detenido.")

class Camion(Vehiculo):
    def __init__(self, marca, modelo, año, capacidad_carga):
        super().__init__(marca, modelo, año)
        self.__capacidad_carga = capacidad_carga

    def get_capacidad_carga(self):
        return self.__capacidad_carga

    def set_capacidad_carga(self, capacidad_carga):
        self.__capacidad_carga = capacidad_carga

    def acelerar(self):
        print(f"El camión {self.get_marca()} {self.get_modelo()} con capacidad de carga de {self.get_capacidad_carga()} kg está acelerando.")
    
    def detener(self):
        print(f"El camión {self.get_marca()} {self.get_modelo()} se ha detenido.")

if __name__ == "__main__":
    vehiculos = {
        "Corolla": Auto("Toyota", "Corolla", 2020, 4),
        "MT-07": Motocicleta("Yamaha", "MT-07", 2019, 689),
        "Actros": Camion("Volvo", "NO SE MODELOS DE CAMIONES", 2018, 18000)
    }

    for modelo, vehiculo in vehiculos.items():
        vehiculo.acelerar()

    for modelo, vehiculo in vehiculos.items():
        vehiculo.detener()

# en respuesta a la pregunta, para mi el codigo esta bien, desconozco en que se podria mejorar.