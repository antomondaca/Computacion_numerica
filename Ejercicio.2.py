#----- EJERCICIO EN CLASE COMPU NUMERICA LAB ----
# integrante : Antonella Mondaca Alamo
# fecha: 21 de agosto 2026

def descomposicion(x):
    n = str(x)
    base = 10
    cifra_sig = len(n) - 1
    p = float(x) / (base ** cifra_sig)
    return [p, base, cifra_sig, x]

def operacion(n1, n2, opcion):
    a = n1[3]
    b = n2[3]
    match opcion:
        case "+":
            resultado = a + b
            return n1, n2, descomposicion(resultado)
        case "-":
            resultado = a - b
            return n1, n2, descomposicion(resultado)
        case "*":
            resultado = a * b
            return n1, n2, descomposicion(resultado)
        case "/":
            resultado = a / b
            return n1, n2, descomposicion(resultado)
    
def entrada():
    a = int(input("Ingrese el primer operando: "))
    b = int(input("Ingrese el segundo operando: "))
    c = (input("Ingrese la operacion (+, -, *, /): "))
    return a, b, c

if __name__  == "__main__":
    a, b, c = entrada()
    
    print(operacion(descomposicion(a), descomposicion(b), c))
