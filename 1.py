def sum (s1, s2):
    r = s1 + s2
    return r

def mul (s1, s2):
    r = s1 * s2
    return r

def rest (s1, s2):
    r = s1 - s2
    return r

def div (s1, s2):
    r = s1 / s2
    return r

def main ():
    n1 = int(input("Ingrese numero"))
    n2 = int(input("Ingrese numero"))

    print("Ingrese una opcion")
    print("1- Suma")
    print("2- Multiplicacion")
    print("3- Resta")
    print("4- Division")
    opcion = int(input("Ingrese la opcion"))

    if opcion <= 0 or opcion >= 5:
        print("Error, opcion no disponible")

    elif opcion == 1:
        print(sum(n1, n2))
              
    elif opcion == 2:
        print(mul(n1, n2))
              
    elif opcion == 3:
        print(rest(n1, n2))
              
    elif opcion == 4:
        print(div(n1, n2))
              
    return

main()
