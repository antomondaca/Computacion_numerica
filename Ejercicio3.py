#----- EJERCICIO EN CLASE COMPU NUMERICA LAB ----
# integrante : Antonella Mondaca Alamo
# fecha: 04 de septiembre 2026

class biseccion:

    def __init__(self, f, a, b, tol):
        self.f = f
        self.a = a
        self.b = b
        self.tol = tol

    def metodo_biseccion(self):
        if self.f(self.a) * self.f(self.b) >= 0:
            print("El método de bisección no es aplicable.")
            return None

        while (self.b - self.a) / 2 > self.tol:
            c = (self.a + self.b) / 2
            if self.f(c) == 0:
                return c
            elif self.f(self.a) * self.f(c) < 0:
                self.b = c
            else:
                self.a = c

        return (self.a + self.b) / 2
    
def main():
    return

if __name__ == "__main__":
    main()
