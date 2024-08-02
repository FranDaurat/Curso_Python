#!/usr/bin/python3

class Vehiculo:

    def __init__(self, matricula, modelo):
        self.matricula = matricula
        self.modelo = modelo
        self.disponible = True

    def __str__(self):
        return f"Vehiculo(matriculo={self.matricula}), modelo={self.modelo}, disponible={self.disponible}"

    def alquilar(self):
        if self.disponible:
            self.disponible = False
        else:
            print(f"\n[!] El vehiculo con matricula {self.matricula} no se puede alquilar")
    
    def devolver(self):
        if not self.disponible :
            self.disponible = True
        else:
            print(f"\n[!] El vehiculo con matricula {self.matricula} no se puede devolver")


class Flota:

    def __init__(self):
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def __str__(self):
        return "\n".join(str(vehiculo) for vehiculo in self.vehiculos)

    def alquilar_vehiculo(self, matricula):
        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                vehiculo.alquilar()

    def devolver_vehiculo(self, matricula):
        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                vehiculo.devolver()

if __name__ == '__main__':

    flota = Flota()

    flota.agregar_vehiculo(Vehiculo("ABSAS", "Toyota Corolla"))
    flota.agregar_vehiculo(Vehiculo("ABSASS", "Honda Civic"))

    print("\n[+] Flota inicial:\n")
    print(flota)

    flota.alquilar_vehiculo("ABSAS")
    print(flota)

    flota.devolver_vehiculo("ABSAS")
    print(flota)