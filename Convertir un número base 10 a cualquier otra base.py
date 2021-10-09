def convertirBase(numeroDecimal,base):
    digitos = "0123456789ABCDEF"

    pilaResiduo = []#en la pila se guarda el resibuo de la division del numero base 10 entre la base que se pida

    while numeroDecimal > 0:
        residuo = numeroDecimal % base
        pilaResiduo.append(residuo)#el residuo optenido  de la division de numero base 10/base, sw guarda en la pilaResiduo
        numeroDecimal = numeroDecimal // base
     
    nuevaCadena = ""
    for i in range(len(pilaResiduo)):#la longitud y el rango determinado
        nuevaCadena = nuevaCadena + digitos[pilaResiduo.pop()]# se añade lo a la nueva cadena los digitos restantes que se eliminaron de la pila
        
    return nuevaCadena

print(convertirBase(8,2))
print(convertirBase(15,8))